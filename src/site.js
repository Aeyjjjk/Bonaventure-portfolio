(function(){
'use strict';
var $=function(s,r){return (r||document).querySelector(s)},$$=function(s,r){return Array.prototype.slice.call((r||document).querySelectorAll(s))};
var ST={
  get:function(k){var v=null;try{v=localStorage.getItem('pf-'+k);}catch(e){}
    if(v)return v;try{var m=(window.name||'').match(new RegExp('pf-'+k+'=([a-z]+)'));return m?m[1]:null;}catch(e){return null;}},
  set:function(k,v){try{localStorage.setItem('pf-'+k,v);}catch(e){}
    try{var n=(window.name||'').replace(new RegExp('pf-'+k+'=[a-z]+;?'),'');window.name=n+'pf-'+k+'='+v+';';}catch(e){}}
};
var reduce=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;

/* mobile menu */
var mb=$('.menu-btn'),nl=$('#navlist');
if(mb&&nl){
  mb.addEventListener('click',function(){var o=nl.classList.toggle('open');mb.setAttribute('aria-expanded',o);});
  $$('a',nl).forEach(function(a){a.addEventListener('click',function(){nl.classList.remove('open');mb.setAttribute('aria-expanded','false');});});
  document.addEventListener('keydown',function(e){if(e.key==='Escape'&&nl.classList.contains('open')){nl.classList.remove('open');mb.setAttribute('aria-expanded','false');mb.focus();}});
}

/* scroll progress */
var bar=$('.progress');
function prog(){if(!bar)return;var h=document.documentElement.scrollHeight-innerHeight;bar.style.transform='scaleX('+(h>0?Math.min(1,scrollY/h):0)+')';}
addEventListener('scroll',prog,{passive:true});prog();

/* scrollspy: nav links (home) and table of contents (case studies) */
function spy(links,attr){
  if(!links.length||!('IntersectionObserver' in window))return;
  var map={};links.forEach(function(a){var id=a.getAttribute('href').split('#')[1];if(id){var el=document.getElementById(id);if(el)map[id]={a:a,el:el};}});
  var ids=Object.keys(map);if(!ids.length)return;
  function update(){
    var y=scrollY+140,cur=null;
    ids.forEach(function(id){if(map[id].el.offsetTop<=y)cur=id;});
    links.forEach(function(a){a.removeAttribute(attr==='aria-current'?'aria-current':'x');a.classList.remove('on');});
    if(cur){var a=map[cur].a;if(attr==='aria-current')a.setAttribute('aria-current','true');else a.classList.add('on');}
  }
  addEventListener('scroll',update,{passive:true});update();
}
spy($$('.nav ul a[href*="#"]').filter(function(a){return !/^(https?:)?\/\//.test(a.getAttribute('href'))&&document.getElementById((a.getAttribute('href').split('#')[1]||'__'))}),'aria-current');
spy($$('.toc a'),'on');

/* project filter */
var fchips=$$('.filters .chip');
fchips.forEach(function(c){c.addEventListener('click',function(){
  fchips.forEach(function(x){x.setAttribute('aria-pressed',x===c)});
  var f=c.getAttribute('data-f'),n=0;
  $$('.card[data-d]').forEach(function(k){var ok=f==='all'||k.getAttribute('data-d').split(' ').indexOf(f)>-1;k.hidden=!ok;if(ok)n++;});
  var st=$('#filter-status');if(st)st.textContent=n+(n===1?' investigation shown':' investigations shown');
});});

/* methodology tabs */
$$('.mw').forEach(function(w){
  var mt=$$('.method [role="tab"]',w),mp=$('.method-panel',w),dj=$('.mdata',w);
  if(!mt.length||!mp||!dj)return;
  var M=JSON.parse(dj.textContent);
  function sel(i,focus){mt.forEach(function(t,j){t.setAttribute('aria-selected',i===j);t.tabIndex=i===j?0:-1;});
    mp.innerHTML='<h3></h3><p></p>';$('h3',mp).textContent=M[i].t;$('p',mp).textContent=M[i].d;if(focus)mt[i].focus();}
  mt.forEach(function(t,i){t.addEventListener('click',function(){sel(i)});
    t.addEventListener('keydown',function(e){var k=e.key;if(k==='ArrowRight'||k==='ArrowDown'){e.preventDefault();sel((i+1)%mt.length,1)}else if(k==='ArrowLeft'||k==='ArrowUp'){e.preventDefault();sel((i+mt.length-1)%mt.length,1)}});});
  sel(0);
});

/* theme toggle */
var tbtn=$('.theme-btn'),de=document.documentElement;
function setTheme(t,save){
  if(t==='light')de.setAttribute('data-theme','light');else de.setAttribute('data-theme','dark');
  if(tbtn)tbtn.setAttribute('aria-pressed',t==='light');
  if(save)ST.set('theme',t);
}
var th='dark';th=ST.get('theme')||(de.getAttribute('data-theme')==='light'?'light':'dark');
setTheme(th,false);
if(tbtn)tbtn.addEventListener('click',function(){setTheme(de.getAttribute('data-theme')==='light'?'dark':'light',true);});

/* role switcher */
var root=$('.rr'),ROLES=['electrical','forensics','soc'];
function setRole(r,fromUser){
  if(ROLES.indexOf(r)<0)return;
  if(root)root.setAttribute('data-role',r);
  $$('[data-role-btn]').forEach(function(b){b.setAttribute('aria-pressed',b.getAttribute('data-role-btn')===r);});
  ST.set('role',r);
  var pr=$('[data-pagerole]');
  if(fromUser&&pr&&pr.getAttribute('data-pagerole')!==r){location.href='index.html';}
}
var init='forensics',pr0=$('[data-pagerole]');
init=ST.get('role')||init;
if(pr0)init=pr0.getAttribute('data-pagerole');
setRole(init,false);
$$('[data-role-btn]').forEach(function(b){b.addEventListener('click',function(){setRole(b.getAttribute('data-role-btn'),true);});});

/* profile photos: one per role; show only files that exist (falls back to profile.webp) */
function photoState(){
  $$('.pframe,.portrait .frame').forEach(function(f){
    var any=$$('.pimg',f).some(function(im){return im.dataset.ok==='1'&&im.offsetParent!==null;});
    f.classList.toggle('has',any);
  });
}
$$('.pimg').forEach(function(im){
  function ok(){im.dataset.ok='1';im.hidden=false;photoState();}
  im.addEventListener('load',function(){if(im.naturalWidth>0)ok();});
  im.addEventListener('error',function(){
    var fb=im.getAttribute('data-fb');
    if(fb&&!im.dataset.tried){im.dataset.tried='1';im.src=fb;}else{im.hidden=true;im.dataset.ok='0';photoState();}
  });
  if(im.complete&&im.naturalWidth>0)ok();
});
var _sr=setRole;setRole=function(r,u){_sr(r,u);photoState();};

/* tool cards */
$$('.skillcat').forEach(function(cat){
  var d=$('.tooldesc',cat),tools=$$('.tool',cat);
  tools.forEach(function(t){t.addEventListener('click',function(){
    tools.forEach(function(x){x.setAttribute('aria-expanded',x===t)});
    d.innerHTML='';var b=document.createElement('b');b.textContent=t.textContent+'. ';d.appendChild(b);d.appendChild(document.createTextNode(t.getAttribute('data-how')));
  });});
  if(tools[0])tools[0].click();
});

/* toast */
var toast=$('.toast');var tt;
function say(m){if(!toast)return;toast.textContent=m;toast.classList.add('show');clearTimeout(tt);tt=setTimeout(function(){toast.classList.remove('show')},3800);}
$$('[data-soon]').forEach(function(a){a.addEventListener('click',function(e){e.preventDefault();say(a.getAttribute('data-soon'));});});

/* lightbox */
var shots=$$('[data-lb]');
if(shots.length){
  var lb=document.createElement('div');lb.className='lb';lb.setAttribute('role','dialog');lb.setAttribute('aria-modal','true');lb.setAttribute('aria-label','Image viewer');
  lb.innerHTML='<div class="lb-bar"><span class="cnt" aria-live="polite"></span><div class="lb-btns"><button type="button" data-a="prev" aria-label="Previous image">&larr;</button><button type="button" data-a="next" aria-label="Next image">&rarr;</button><button type="button" data-a="size" aria-label="Toggle actual size">1:1</button><button type="button" data-a="close" aria-label="Close viewer">Close</button></div></div><div class="lb-stage"><img alt=""></div><div class="lb-cap"></div>';
  document.body.appendChild(lb);
  var img=$('img',lb),cap=$('.lb-cap',lb),cnt=$('.cnt',lb),idx=0,last=null;
  function show(i){idx=(i+shots.length)%shots.length;var s=shots[idx];img.classList.remove('nat');img.src=s.getAttribute('data-lb');img.alt=s.getAttribute('data-alt')||'';cap.textContent=s.getAttribute('data-cap')||'';cnt.textContent=(idx+1)+' / '+shots.length;}
  function open(i){last=document.activeElement;show(i);lb.classList.add('open');document.body.style.overflow='hidden';$('[data-a=close]',lb).focus();}
  function close(){lb.classList.remove('open');document.body.style.overflow='';if(last)last.focus();}
  shots.forEach(function(s,i){s.addEventListener('click',function(){open(i)});});
  lb.addEventListener('click',function(e){var a=e.target.getAttribute&&e.target.getAttribute('data-a');
    if(a==='close'||e.target===$('.lb-stage',lb))close();else if(a==='prev')show(idx-1);else if(a==='next')show(idx+1);else if(a==='size')img.classList.toggle('nat');});
  document.addEventListener('keydown',function(e){if(!lb.classList.contains('open'))return;
    if(e.key==='Escape')close();else if(e.key==='ArrowLeft')show(idx-1);else if(e.key==='ArrowRight')show(idx+1);
    else if(e.key==='Tab'){var f=$$('button',lb),fi=f.indexOf(document.activeElement);if(e.shiftKey&&fi<=0){e.preventDefault();f[f.length-1].focus()}else if(!e.shiftKey&&fi===f.length-1){e.preventDefault();f[0].focus()}}});
}

/* contact form: validation and confirmation state. No message is sent. */
var form=$('#contact-form');
if(form){
  var ok=$('#form-ok');
  function bad(id,on){var f=$('#'+id).closest('.field');f.classList.toggle('bad',on);$('#'+id).setAttribute('aria-invalid',on);}
  form.addEventListener('submit',function(e){
    e.preventDefault();
    var n=$('#f-name').value.trim(),m=$('#f-mail').value.trim(),t=$('#f-msg').value.trim();
    var vn=n.length>1,vm=/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(m),vt=t.length>=10;
    bad('f-name',!vn);bad('f-mail',!vm);bad('f-msg',!vt);
    if(!(vn&&vm&&vt)){var first=$('.field.bad input,.field.bad textarea',form);if(first)first.focus();return;}
    form.hidden=true;ok.classList.add('show');ok.focus();
  });
  var again=$('#form-again');if(again)again.addEventListener('click',function(){form.reset();form.hidden=false;ok.classList.remove('show');$('#f-name').focus();});
}

/* collapsible home sections: closed until the reader scrolls to them (or presses the button) */
var folds=$$('[data-fold]');
if(folds.length){
  folds.forEach(function(sec){
    $$('.sec-head',sec).forEach(function(head){
      var body=document.createElement('div'),inn=document.createElement('div');
      body.className='fold-body';inn.className='fold-in';
      while(head.nextSibling)inn.appendChild(head.nextSibling);
      body.appendChild(inn);head.parentNode.appendChild(body);
      var btn=document.createElement('button');btn.type='button';btn.className='fold-btn';btn.setAttribute('aria-expanded','false');
      btn.innerHTML='<span class="o">Show section</span><span class="c">Hide section</span>';
      btn.addEventListener('click',function(){setFold(sec,!sec.classList.contains('open'));sec.setAttribute('data-manual','1');});
      head.appendChild(btn);
    });
    sec.classList.add('fold-ready');
  });
  function setFold(sec,open){sec.classList.toggle('open',open);$$('.fold-btn',sec).forEach(function(b){b.setAttribute('aria-expanded',open);});}
  var hold=false,ht=null,fo=null;
  if('IntersectionObserver' in window){
    fo=new IntersectionObserver(function(es){es.forEach(function(e){
      if(hold||!e.isIntersecting||e.target.getAttribute('data-manual'))return;
      setFold(e.target,true);fo.unobserve(e.target);
    });},{rootMargin:'0px 0px -30% 0px'});
    folds.forEach(function(s){fo.observe(s);});
  }else{folds.forEach(function(s){setFold(s,true);});}
  /* a jump to a section opens only that section, so the page does not shift while it scrolls */
  function jump(id){
    var t=id&&document.getElementById(id);if(!t)return;
    var sec=t.hasAttribute('data-fold')?t:(t.closest?t.closest('[data-fold]'):null);
    hold=true;
    if(sec){sec.classList.add('noanim');setFold(sec,true);if(fo)fo.unobserve(sec);setTimeout(function(){sec.classList.remove('noanim');},60);}
    clearTimeout(ht);
    ht=setTimeout(function(){hold=false;if(fo)folds.forEach(function(s){if(!s.classList.contains('open')){fo.unobserve(s);fo.observe(s);}});},1400);
  }
  document.addEventListener('click',function(e){
    var a=e.target.closest?e.target.closest('a[href^="#"]'):null;
    if(a)jump(a.getAttribute('href').slice(1));
  });
  if(location.hash)jump(location.hash.slice(1));
}
})();
