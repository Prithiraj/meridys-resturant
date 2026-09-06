import http from 'node:http';
import fs from 'node:fs/promises';
import path from 'node:path';
import zlib from 'node:zlib';
export async function startServer() {
  const root = path.resolve('_site');
  const prefix = '/meridys-resturant';
  const mime = {'.html':'text/html; charset=utf-8','.css':'text/css; charset=utf-8','.js':'text/javascript; charset=utf-8','.webp':'image/webp','.jpg':'image/jpeg','.png':'image/png','.svg':'image/svg+xml','.json':'application/json','.xml':'application/xml','.txt':'text/plain'};
  const server = http.createServer(async (req,res) => {
    try {
      let pathname = decodeURIComponent(new URL(req.url,'http://localhost').pathname);
      if (!pathname.startsWith(prefix+'/')) { res.writeHead(404).end(); return; }
      pathname = pathname.slice(prefix.length);
      if (pathname.endsWith('/')) pathname += 'index.html';
      const file = path.resolve(root,'.'+pathname);
      if (!file.startsWith(root+path.sep)) {res.writeHead(403).end();return;}
      let data = await fs.readFile(file);
      const ext = path.extname(file);
      const headers = {'Content-Type':mime[ext]||'application/octet-stream','Cache-Control':'no-cache'};
      if (/html|css|js|svg|json/.test(ext) && req.headers['accept-encoding']?.includes('gzip')) {data=zlib.gzipSync(data);headers['Content-Encoding']='gzip';}
      res.writeHead(200,headers).end(data);
    } catch { res.writeHead(404).end('Not found'); }
  });
  await new Promise(resolve=>server.listen(4173,'127.0.0.1',resolve));
  return {server, url:'http://127.0.0.1:4173'+prefix+'/'};
}
