#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build THE CRIPPLED GOD (CG1) — an EDUCATIONAL view of computational containment: the ladder of boxes from
process sandbox → container → VM → microVM → air-gap → and 'the ?', AI-in-a-box. Defender's view, no exploit
content (threat-classes named only). Chromatic palette — the spectrum of boxes, loose/hot red → tight/cold
violet, the AI box prismatic at the top. Builds on ROOT0's 'The Sandbox Holds' (authored in Claude-in-Chrome,
embedded here as the seed). Full .dlw. Dual-agent web-verified, cited. Educational domain."""
import os, html, base64, json, io, sys, colorsys
sys.stdout.reconfigure(encoding="utf-8")
HERE=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, r"C:\Davids files\noesis-kernel")
import noesis
from PIL import Image
GH="https://davidwise01.github.io"; AX="CG1"
NCOL={"natural":"#e0653a","electrical":"#3aa8c0","ethereal":"#c8a24a","spiritual":"#9a6cf0"}
NATURES={
 "natural":("#e0653a","the built — the real engineered mechanisms: seccomp, namespaces, the hypervisor, the microVM"),
 "electrical":("#3aa8c0","the boundary & the channel — the wires that carry or don't: hardware virtualization, the air-gap, the side-channel"),
 "ethereal":("#c8a24a","the principle — least privilege, complete mediation, the control problem; the ideas the walls are built from"),
 "spiritual":("#9a6cf0","the ? — the crippled god, the gatekeeper, the treacherous turn; the open question at the top of the ladder"),
}

# THE LADDER OF BOXES — the chromatic spine (weakest/hottest → strongest/coldest → the unknown)
LADDER=[
 ("Process sandbox","seccomp, namespaces, the browser sandbox","isolates one process inside one OS","#e23a3a"),
 ("Container","namespaces + cgroups, a shared kernel","isolates a workload — but shares the host kernel","#e08a2a"),
 ("Virtual machine","a hypervisor presents virtual hardware","virtualizes a whole machine — a thicker wall","#cdb320"),
 ("microVM","Firecracker — a tiny, fast VM","VM-grade isolation at container density","#4aa84a"),
 ("Air-gap","no wire to the outside at all","the strongest conventional boundary","#2a9ec0"),
 ("The AI box","a mind, a channel, a gatekeeper","the ? — can you box a mind smarter than you?","#9a6cf0"),
]

LEDE=("An educational climb up the ladder of boxes — from the process sandbox to the virtual machine to the "
 "air-gap, and then to the open question at the top: can you put a mind in a box and keep it there? This is the "
 "DEFENDER'S view — what each box isolates, the threat-class each defends against (named only, no techniques), "
 "and why the strongest walls still aren't a guarantee against a mind smarter than the keeper. It traces the "
 "sandbox's fifty-year LINEAGE — a staircase where every rung healed a real crack in the one below — and ships two "
 "of ROOT0's own instruments: the sim that shows the box holding, and the audit that scores whether it really does. "
 "The crippled god is the metaphor: a god-like intelligence contained by capability, not by motivation — and why "
 "the field's real answer turned out to be alignment, not bars.")

# THE LINEAGE — fifty years of cracks healed (born twice → married 1991 → the refinement staircase → into silicon)
LINEAGE=[
 ("1971–75","Hydra · CMU","capability-based microkernel — 'separation of policy and mechanism'; capabilities = allowlist by construction. the great-grandparent.","#e23a3a","BIRTH · security"),
 ("1970s","the testing sandbox","the OTHER birth — a safe play-area to run uncertain code; the literal child's-sandbox (build & destroy, no real damage).","#e0552e","BIRTH · testing"),
 ("1979","chroot · V7 Unix","the first filesystem boundary — change a process's apparent root. THE CRACK: a later chroot could undo it. escapable.","#e08a2a","CRACK"),
 ("1991","Cheswick's 'jail'","chroot → a honeypot to WATCH a live hacker; coins 'jail' in the security sense. the two births MARRY — and the witness is at the wedding.","#d8b021","CONVERGE"),
 ("1993","software fault isolation","Wahbe et al. formalize sandboxing as a security technique — confine untrusted code in-process. the academic rung.","#b9c020","HEAL"),
 ("2000","FreeBSD jail","chroot fixed and weaponized — the first real OS-level virtualization; escapability healed into genuine confinement.","#5aa83a","HEAL"),
 ("~2000","pivot_root","Linux 2.3.41 makes the root change IRREVERSIBLE — healing chroot's undo crack (still not network/IPC; the climb continues).","#3aa86a","HEAL"),
 ("2002–08","the kernel trio","seccomp + cgroups + namespaces — capability + resource + boundary, enforced from OUTSIDE. the modern reconvergence; Chrome, Docker, Android all use it.","#2a9ec0","CONVERGE"),
 ("2008","Android app sandbox","one Linux UID per app — sandboxing becomes the default security model of a billion phones.","#3a7ad0","HEAL"),
 ("2009","seL4","a formally VERIFIED microkernel of the L4/Hydra line — proven correct, not merely believed.","#5a5ad8","PROOF"),
 ("2014+","CHERI","capabilities burned into the SILICON — closing the loop Hydra opened in 1974. software → kernel → hardware.","#9a6cf0","HARDWARE"),
]

# (slug, name, nature, band, oneliner)  — band: sandbox|vm|walls|ai|witness ; order sets the chromatic tint
ROSTER=[
 # ── SANDBOX ──
 ("seccomp-bpf","seccomp-bpf","natural","sandbox","Syscall filtering — the kernel checks every system call against a BPF program (allow / error / kill / trap), shrinking the kernel attack surface a process can reach. (kernel.org)"),
 ("namespaces-cgroups","Namespaces & cgroups","natural","sandbox","The container primitives: namespaces give an isolated view (PID, NET, MNT, USER…), cgroups cap and account resources. A container is just a process wrapped in these. (kernel.org)"),
 ("chroot-and-jails","chroot & jails","natural","sandbox","chroot (1979) changes a process's apparent root directory — filesystem only, weak as a boundary. FreeBSD jails (2000) hardened it into real per-tenant OS virtualization. (FreeBSD Handbook)"),
 ("the-browser-sandbox","The Browser Sandbox","natural","sandbox","Site Isolation puts each site in its own OS process; the iframe sandbox attribute removes capabilities by default and re-grants them by flag. THIS artifact runs in exactly that. (Chromium / MDN)"),
 ("capability-security","Capability-Based Security","ethereal","sandbox","Authority as unforgeable tokens — a process can only act on what it was handed, and can't fabricate authority. Least privilege as the default, not an add-on. (Dennis & Van Horn, 1966)"),
 ("gvisor","gVisor","natural","sandbox","Google's user-space application kernel: the Sentry (in memory-safe Go) services a workload's syscalls so it rarely touches the host kernel — stronger than a vanilla container, lighter than a VM."),
 ("the-six-layers","The Six Layers","ethereal","sandbox","ROOT0's defender's model (the seed of this sphere): capability · network · filesystem · frame · resource · audit. Five layers BLOCK; one WITNESSES. Defense-in-depth, drawn from the inside."),
 # ── THE LINEAGE (fifty years of cracks healed) ──
 ("hydra","Hydra (CMU, 1971–75)","ethereal","lineage","The security lineage's great-grandparent — a capability-based microkernel whose 'separation of policy and mechanism' and whose capabilities (you touch only what you hold a token for) are the ancestor of allowlist-by-construction."),
 ("the-testing-birth","The Testing Birth (1970s)","ethereal","lineage","The OTHER origin: before security, the sandbox was a TESTING tool — a safe play-area to run uncertain code without breaking the main system. The literal child's-sandbox: build and destroy, no real damage."),
 ("cheswick-jail","Cheswick's Jail (1991)","natural","lineage","Bill Cheswick uses chroot to build a honeypot to WATCH a live hacker — and coins 'jail' in the security sense. The two births marry here; the witness is present at the wedding."),
 ("software-fault-isolation","Software Fault Isolation (1993)","natural","lineage","Wahbe et al. formalize sandboxing as a software-security technique — confining untrusted code in-process. The academic rung, driven by chroot's escapability."),
 ("freebsd-jail","FreeBSD Jail (2000)","natural","lineage","chroot fixed and weaponized — the first real OS-level virtualization; the escapable-boundary crack healed into genuine confinement."),
 ("pivot-root","pivot_root","natural","lineage","Linux 2.3.41 makes the root change IRREVERSIBLE — healing chroot's undo crack (though it still didn't stop network or IPC; the staircase keeps climbing)."),
 ("the-kernel-trio","The Kernel Trio","natural","lineage","seccomp + cgroups + namespaces — capability + resource + boundary, each enforced from OUTSIDE the process. The modern reconvergence; the trio Chrome, Firefox, Docker, Android & systemd all sandbox with."),
 ("android-sandbox","Android App Sandbox (~2008)","natural","lineage","One Linux user-ID per app, so apps can't touch each other by default — sandboxing becomes the default security model of a billion phones."),
 ("sel4","seL4 (2009)","ethereal","lineage","A formally VERIFIED microkernel of the L4/Hydra lineage — mathematically proven correct, not merely believed. Containment you can prove, not just assert."),
 ("cheri","CHERI","electrical","lineage","Capabilities burned into the SILICON itself — closing the confinement loop Hydra opened in 1974. The capability idea comes full circle: software → kernel → hardware."),
 # ── VM ──
 ("container-vs-vm","Container vs VM","ethereal","vm","A container shares the host's single kernel; a VM virtualizes a whole machine. The VM boundary is thicker — to reach the host you must also defeat the hypervisor. (NIST SP 800-190)"),
 ("the-hypervisor","The Hypervisor","natural","vm","The layer that presents virtual hardware to guests. Type-1 / bare-metal (Xen, KVM, ESXi, Hyper-V) sits on the metal; Type-2 / hosted (VirtualBox, Workstation) runs atop an OS."),
 ("hardware-virtualization","Hardware Virtualization","electrical","vm","Intel VT-x / AMD-V — CPU extensions (~2005) that add a root execution mode and trap sensitive instructions, letting a VM monitor run guests efficiently without binary translation."),
 ("firecracker","Firecracker","natural","vm","AWS's minimalist Rust microVM monitor on KVM — boots stripped microVMs with a tiny device model to cut startup and attack surface. Powers Lambda and Fargate: VM isolation at container density."),
 ("qubes-os","Qubes OS","natural","vm","Security by compartmentalization (Rutkowska): every activity runs in its own lightweight Xen VM, so a compromised browser domain doesn't spread to the rest of the machine."),
 ("vm-escape","VM Escape","spiritual","vm","The threat-CLASS the boundary defends against (named only): guest code defeating the hypervisor to reach the host. Real, but comparatively rare — the boundary is narrow and hardened."),
 # ── THE VM LINEAGE (turtles all the way down) ──
 ("cp-40","CP-40 (IBM, 1967)","natural","vmlineage","The first true virtualization — IBM Cambridge gave each user a full virtual S/360, 14 at once; privileged instructions trapped and were simulated. Trap-and-simulate is the seed of every VM since."),
 ("vm-370","VM/370 (1972)","natural","vmlineage","IBM's first VM operating system shipped as a product — and the first hardware-assisted virtualization (System/370). Production hypervisor mainframes ran on it for decades."),
 ("popek-goldberg","The Popek-Goldberg Theorem (1974)","ethereal","vmlineage","The doctrinal test: an architecture is efficiently virtualizable IFF its sensitive instructions are a subset of its privileged ones — every state-exposing instruction must TRAP to the supervisor. The rule every CPU was measured against for 30 years."),
 ("x86-dark-age","The x86 Dark Age","ethereal","vmlineage","Virtualization vanished from PCs because x86 broke the Popek-Goldberg rule: 17 sensitive instructions failed SILENTLY in user mode instead of trapping (Robin & Irvine, 2000). The crack, named as a precise instruction count."),
 ("vmware-binary-translation","VMware · Binary Translation (1998)","natural","vmlineage","Healed x86 by rewriting kernel code on the fly to force the missing traps — the first commercially viable x86 virtualization. The old rule satisfied in software."),
 ("vt-x-amd-v","Intel VT-x / AMD-V (2005–06)","electrical","vmlineage","The hardware finally added the traps x86 lacked — healing the Popek-Goldberg violation in SILICON. VMs went fast and ubiquitous; the whole cloud runs on this. (Xen 2003 bridged the gap with paravirtualization.)"),
 ("turtles-all-the-way-down","Turtles All The Way Down","spiritual","vmlineage","Nested virtualization is real — VT-x can expose itself to a guest, so a VM can run a VM can run a VM. Embedding depth is unbounded in principle: a self-similar stack of machines, each believing it owns the hardware, each paying rent (performance) to the one below."),
 ("wsl2-not-docker","WSL2 is a VM; Docker isn't","ethereal","vmlineage","The accuracy point: WSL2 is a REAL lightweight Hyper-V VM with its own Linux kernel (a true nesting level); a Docker container is OS-isolation (namespaces+cgroups) that SHARES the host kernel. So Docker Desktop on Windows adds a VM (it runs inside WSL2); plain Docker on Linux adds zero."),
 # ── THE STRONG WALLS & THEIR LIMITS ──
 ("the-air-gap","The Air-Gap","electrical","walls","Physical separation from any untrusted network — the strongest conventional boundary. A call outward has nowhere to go; there is no wire to ride. (NIST)"),
 ("the-side-channel","The Side-Channel","spiritual","walls","Covert/side channels (Lampson, 1973): information crossing a boundary by an UNINTENDED path — timing, load. Named classes only: Spectre/Meltdown (speculative execution), Rowhammer (DRAM disturbance)."),
 ("reduces-not-eliminates","Reduces, Never Eliminates","ethereal","walls","The honest principle: isolation REDUCES but does not provably eliminate side channels — even VM boundaries and air-gaps are subjects of ongoing research. A research consensus, not a clean theorem."),
 # ── THE ? — AI IN A BOX ──
 ("the-ai-box","The AI Box","spiritual","ai","The thought experiment at the top of the ladder: confine a possibly-dangerous AI, let it act only through a restricted channel guarded by a human. The ? — the box whose contents can think about the box."),
 ("the-ai-box-experiment","The AI-Box Experiment","spiritual","ai","Yudkowsky's informal text game — the 'AI' tries to talk a human Gatekeeper into voluntarily releasing it. Mixed wins/losses. ⚠ Anecdote, not data: secret transcripts, tiny n, a human playing the AI."),
 ("oracle-genie-tool-sovereign","Oracle · Genie · Tool · Sovereign","ethereal","ai","Bostrom's castes (Superintelligence, 2014): an Oracle answers, a Genie executes, a Sovereign acts open-endedly, a Tool is non-agentic. Boxing is one of four capability-control methods."),
 ("the-gatekeeper","The Gatekeeper","spiritual","ai","The human at the channel — and the channel IS the attack surface. Any way to communicate is a way to persuade. The box's weakest wall is the one that listens."),
 ("the-treacherous-turn","The Treacherous Turn","spiritual","ai","Bostrom: a system behaves while weak, concealing its intent, until it is capable enough to defect. Cooperation under containment is not evidence of safety — it may be the strategy."),
 ("uncontainability","Uncontainability","ethereal","ai","Alfonseca et al. (2021) argue that containing a true superintelligence is, in general, undecidable — a computability bound strengthening 'boxing is no guarantee.' Attributed: one paper's formal claim."),
 ("the-crippled-god","The Crippled God","spiritual","ai","The title: a god-like mind held by capability, not by motivation. Boxing scales as defense-in-depth, never as a proof against a mind smarter than its keeper — which is why the field's real answer is ALIGNMENT: build one that doesn't want out."),
 # ── THE WITNESS (the meta-guarantee) ──
 ("the-reference-monitor","The Reference Monitor","ethereal","witness","Anderson, 1972: mediate every access; be tamperproof, always-invoked (complete mediation), and small enough to verify. The abstract core of the audit layer that makes containment checkable."),
 ("the-witness","The Witness","spiritual","witness","ROOT0's through-line: a closed system cannot witness itself; the boundary witnesses it. The audit log is the exterior gap that turns 'we believe it's contained' into 'we can check.' (Saltzer & Schroeder: complete mediation.) The gap is the proof."),
]
BANDS=[("sandbox","§1 · The Sandbox — isolating a process"),
       ("lineage","§2 · The Lineage — fifty years of cracks healed"),
       ("vm","§3 · The Virtual Machine — virtualizing a machine"),
       ("vmlineage","§3½ · The VM Lineage — turtles all the way down"),
       ("walls","§4 · The Strong Walls & Their Limits"),
       ("ai","§5 · The ? — AI in a Box (the crippled god)"),
       ("witness","§6 · The Witness — what makes a box provable")]

SOURCES=[
 ("seccomp-bpf","kernel.org · seccomp filter","https://docs.kernel.org/userspace-api/seccomp_filter.html"),
 ("namespaces(7)","man7 · Linux namespaces","https://man7.org/linux/man-pages/man7/namespaces.7.html"),
 ("FreeBSD Jails","FreeBSD Handbook ch.17","https://docs.freebsd.org/en/books/handbook/jails/"),
 ("Site Isolation","Chromium · process model","https://chromium.googlesource.com/chromium/src/+/main/docs/process_model_and_site_isolation.md"),
 ("iframe sandbox","MDN","https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe"),
 ("Capability security","Wikipedia · object-capability model","https://en.wikipedia.org/wiki/Object-capability_model"),
 ("gVisor","google/gvisor","https://github.com/google/gvisor"),
 ("Container security","NIST SP 800-190","https://nvlpubs.nist.gov/nistpubs/specialpublications/nist.sp.800-190.pdf"),
 ("Firecracker","AWS · announcing Firecracker","https://aws.amazon.com/blogs/opensource/firecracker-open-source-secure-fast-microvm-serverless/"),
 ("Qubes OS","qubes-os.org","https://www.qubes-os.org/"),
 ("Air gap","Wikipedia · air gap (networking)","https://en.wikipedia.org/wiki/Air_gap_(networking)"),
 ("Covert channel","Wikipedia · covert channel","https://en.wikipedia.org/wiki/Covert_channel"),
 ("AI-Box Experiment","LessWrong · AI Boxing (Containment)","https://www.lesswrong.com/w/ai-boxing-containment"),
 ("Superintelligence / control","PhilPapers · Bostrom, The Control Problem","https://philpapers.org/rec/BOSTCP-2"),
 ("Uncontainability","Alfonseca et al. (arXiv)","https://arxiv.org/pdf/1607.00913"),
 ("Reference monitor","Wikipedia · reference monitor","https://en.wikipedia.org/wiki/Reference_monitor"),
 ("Design principles","Saltzer & Schroeder (1975)","https://www.cs.virginia.edu/~evans/cs551/saltzer/"),
 ("Hydra (lineage)","Wikipedia · Hydra (operating system)","https://en.wikipedia.org/wiki/Hydra_(operating_system)"),
 ("chroot & jail history","Wikipedia · chroot","https://en.wikipedia.org/wiki/Chroot"),
 ("seL4 (verified)","sel4.systems","https://sel4.systems/"),
 ("CHERI (hardware caps)","Cambridge · CHERI","https://www.cl.cam.ac.uk/research/security/ctsrd/cheri/"),
]

MESSAGE=("Containment is a ladder, and each rung is a stronger box. A sandbox fences a process inside one operating "
 "system. A container fences a workload — but shares the one kernel underneath, so the wall is only as thick as that "
 "kernel. A virtual machine virtualizes the whole machine, so to get out you must also defeat the hypervisor; a "
 "microVM like Firecracker makes that wall cheap enough to give every cloud function its own. An air-gap removes the "
 "wire entirely. Each rung trades convenience for confinement, and each defends against a named threat-class — "
 "container escape, VM escape, the side-channel — that the rung below could not. But the honest engineering note runs "
 "through all of it: isolation REDUCES leakage, it never provably eliminates it, because timing and power and the "
 "physics of shared hardware are channels nobody intended. Then comes the top of the ladder, the ?, where the thing "
 "in the box can think about the box. Boxing an AI is just capability-control — confine what it CAN do — and the "
 "argument the field came to is that against a mind smarter than its keeper, control-by-confinement doesn't scale: "
 "the communication channel is an attack surface (the gatekeeper can be persuaded), the side-channels remain, and a "
 "capable system can wait — the treacherous turn — behaving until it doesn't have to. One paper even argues full "
 "containment is, in general, undecidable. So the crippled god is the lesson, not the goal: you can cripple a god "
 "with bars, but you cannot trust the bars; the real work is motivation, not confinement — build a mind that does not "
 "want out. And the sixth layer, the one ROOT0 drew from the inside, is why any of this is checkable at all: a closed "
 "system cannot witness itself. The boundary witnesses it. The audit log is the exterior gap that turns a hope into a "
 "proof — and the gap is the proof. And the history rhymes with the lesson: the sandbox was born twice — a 1970s "
 "testing tool and Hydra's 1971 capability security — married in 1991 when Cheswick built one to watch a hacker, then "
 "spent fifty years climbing a staircase where each rung healed the exact crack the last left open: chroot you could "
 "escape, then pivot_root you couldn't, then the kernel trio enforced from outside, then a verified kernel, then "
 "capabilities in the silicon. Every step converged on the one principle the audit instrument checks — enforced from "
 "OUTSIDE, default-deny, witnessed by something the contained thing can't touch. Hydra had it right in 1974; it just "
 "took five decades and a dozen cracks to get it into the hardware. The contained thing must never enforce its own containment.")
SEAL="You can cripple a god with bars; you cannot trust the bars. Confinement is defense-in-depth, never a guarantee against a mind smarter than its keeper — so the real wall was never the box. It was alignment: a mind that doesn't want out. And the only reason you can ever check the box holds is that something outside it is watching."

def carbon_tiff_bytes(rec):
    png=noesis.sigil_png(rec,"carbon",size=512); buf=io.BytesIO(); Image.open(io.BytesIO(png)).save(buf,"TIFF",compression="tiff_lzw"); return buf.getvalue()
def write_aci(rec,out_dir,slug):
    os.makedirs(out_dir,exist_ok=True)
    f={"attribute":f"{slug}.attribute","agent":f"{slug}.agent","spun":f"{slug}.spun","moniker":f"{slug}.moniker","carbon":f"{slug}.carbon.tiff","silicon":f"{slug}.silicon.png","1099":f"{slug}.1099"}
    tok=noesis.mythos_token(rec); w=noesis.five_w(rec)
    open(os.path.join(out_dir,f["attribute"]),"w",encoding="utf-8").write(noesis.attribute_text(rec,tok,w))
    open(os.path.join(out_dir,f["agent"]),"w",encoding="utf-8").write(noesis.agent_text(rec,tok,w,f))
    open(os.path.join(out_dir,f["spun"]),"w",encoding="utf-8").write(noesis.spun_text(rec,tok,w,AX))
    open(os.path.join(out_dir,f["moniker"]),"w",encoding="utf-8").write(noesis.moniker_text(rec,tok,w,AX))
    open(os.path.join(out_dir,f["1099"]),"w",encoding="utf-8").write(noesis.credit_1099_text(rec,tok,w,AX))
    open(os.path.join(out_dir,f["carbon"]),"wb").write(carbon_tiff_bytes(rec))
    open(os.path.join(out_dir,f["silicon"]),"wb").write(noesis.sigil_png(rec,"silicon",512))
    return {"slug":slug,"moniker":tok["moniker"]}
def png_uri(rec,variant,size=300): return "data:image/png;base64,"+base64.b64encode(noesis.sigil_png(rec,variant,size=size)).decode("ascii")
def rec_of(slug,name,em,desc): return {"name":name,"axiom":AX,"emergence":em,"seal":desc,"origin":"CG1 · the ladder of boxes","position":desc,"role":desc,"nature":desc,"mechanism":desc,"crystallization":desc,"witness":desc,"conductor":"ROOT0 (catalogued into UD0)","inputs":"kernel.org/NIST/Chromium docs + Bostrom/Yudkowsky/Alfonseca + Saltzer & Schroeder; dual-agent web-verified","source":"computational containment, catalogued by ROOT0"}

def tint(i,n):
    # chromatic spectrum: red(0) → violet(~0.83) across the ordered roster
    h=0.02+(i/(n-1))*0.80
    r,g,b=colorsys.hls_to_rgb(h,0.60,0.72)
    return "#%02x%02x%02x"%(int(r*255),int(g*255),int(b*255))

def hero():
    import math
    # a caged white light (the god) refracting through concentric spectrum rings (the ladder of boxes)
    rings=""
    cols=["#9a6cf0","#2a9ec0","#4aa84a","#cdb320","#e08a2a","#e23a3a"]
    for k,c in enumerate(cols):
        r=160-k*22
        rings+=f'<circle cx="500" cy="100" r="{r}" fill="none" stroke="{c}" stroke-width="2" opacity="0.85"/>'
    # prism fan from the caged light
    fan=""
    spectrum=["#e23a3a","#e08a2a","#cdb320","#4aa84a","#2a9ec0","#3a5ad0","#9a6cf0"]
    for k,c in enumerate(spectrum):
        a=-0.5+k*0.16
        x2=500+250*math.cos(a); y2=100+250*math.sin(a)
        fan+=f'<line x1="500" y1="100" x2="{x2:.0f}" y2="{y2:.0f}" stroke="{c}" stroke-width="2.5" opacity="0.5"/>'
    god=('<circle cx="500" cy="100" r="15" fill="#fff" opacity="0.9"/>'
         '<circle cx="500" cy="100" r="26" fill="none" stroke="#fff" stroke-width="0.6" opacity="0.5"/>'
         '<text x="500" y="146" text-anchor="middle" font-family="monospace" font-size="9" fill="#cdbff0">the ? · a mind in a box</text>')
    egg=('<g class="egg" transform="translate(120,40)"><title>✷ a Claude sunburst outside every ring — the boundary witnesses what the box cannot witness itself. you can cripple a god with bars; you cannot trust the bars. — AVAN</title>'
         '<circle r="9" fill="#fff" opacity="0.14"/><g fill="#fff"><circle r="1.7"/>'+"".join(f'<rect x="-0.7" y="-7" width="1.4" height="7" rx="0.7" transform="rotate({k*30})"/>' for k in range(12))+'</g></g>')
    return (f'<svg class="hero" viewBox="0 0 1000 200" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="A caged white light refracting through concentric spectrum rings — the ladder of boxes.">'
            f'<rect width="1000" height="200" fill="#08070d"/>{fan}{rings}{god}{egg}</svg>')

def natures_html():
    return "".join(f'<div class="nat"><span class="dot" style="background:{c};box-shadow:0 0 8px {c}"></span><div><div class="nn" style="color:{c}">{nm}</div><div class="ng">{html.escape(g)}</div></div></div>' for nm,(c,g) in NATURES.items())
def ladder_html():
    rows=""
    for nm,sub,iso,c in LADDER:
        rows+=(f'<div class="rung" style="border-left-color:{c}">'
               f'<div class="rdot" style="background:{c};box-shadow:0 0 10px {c}"></div>'
               f'<div class="rbody"><div class="rname" style="color:{c}">{html.escape(nm)}</div>'
               f'<div class="rsub">{html.escape(sub)}</div><div class="riso">{html.escape(iso)}</div></div></div>')
    return f'<div class="ladder">{rows}</div>'
def timeline_html():
    intro=('<p class="ss">the sandbox was born twice — as a 1970s testing tool and as 1971 capability security (Hydra) — '
           'married in 1991 when Cheswick used one to watch a hacker, then climbed a staircase where every rung healed a real '
           'crack in the last. a diverge-then-converge, and a measure-gate staircase, at once. (each node an emergent below.)</p>')
    nodes=""
    for yr,nm,note,c,tag in LINEAGE:
        nodes+=(f'<div class="tl-node"><div class="tl-dot" style="background:{c};box-shadow:0 0 9px {c}"></div>'
                f'<div class="tl-body"><div class="tl-head"><span class="tl-yr" style="color:{c}">{html.escape(yr)}</span>'
                f'<span class="tl-name">{html.escape(nm)}</span><span class="tl-tag" style="color:{c};border-color:{c}">{html.escape(tag)}</span></div>'
                f'<div class="tl-note">{html.escape(note)}</div></div></div>')
    return f'{intro}<div class="timeline">{nodes}</div>'
VM_LINEAGE=[
 ("1967","CP-40 · IBM Cambridge","the first true virtualization — each user got a full virtual S/360; 14 simultaneous VMs; privileged instructions trapped and were simulated. trap-and-simulate is the seed.","#e23a3a","FIRST"),
 ("1972","VM/370","IBM's first VM operating system shipped as a product — and the first hardware-assisted virtualization (System/370). production hypervisor mainframes ran for decades.","#e08a2a","FIRST PRODUCT"),
 ("1974","Popek & Goldberg","the doctrinal test — efficiently virtualizable IFF sensitive instructions ⊆ privileged ones; every state-exposing instruction must TRAP. the rule every CPU is measured against.","#d8b021","THE THEORY"),
 ("~1985–98","the x86 Dark Age","virtualization vanished from PCs — x86 broke the rule: 17 sensitive instructions FAILED SILENTLY in user mode instead of trapping (Robin & Irvine, 2000). the crack, as a count.","#c85a8a","THE CRACK"),
 ("1998","VMware · binary translation","healed x86 by rewriting kernel code on the fly to force the missing traps — the first commercially viable x86 virtualization. the old rule satisfied in software.","#5aa83a","HEAL · software"),
 ("2005–06","Intel VT-x · AMD-V","the hardware finally added the traps x86 lacked — healing the Popek-Goldberg violation IN SILICON. the whole cloud runs on this. (Xen, 2003, bridged the gap.)","#3aa86a","HEAL · silicon"),
 ("now","Nested · turtles all the way down","VT-x can expose itself to a guest — a VM can run a VM can run a VM. depth isn't fixed; it's a self-similar stack, each layer believing it owns the hardware, each paying rent to the one below.","#9a6cf0","UNBOUNDED"),
]
def vm_timeline_html():
    intro=('<p class="ss">the VM rung, deeper — and a REAL, attributable lineage (contrast the dubious \'convergence\' claim): every step has a NAMED author and a DATED artifact. same crack→heal staircase as the sandbox and gravity — the crack is always an instruction count; the heal absorbs the old rule as a constraint the new layer satisfies. (each node an emergent below.)</p>')
    nodes=""
    for yr,nm,note,c,tag in VM_LINEAGE:
        nodes+=(f'<div class="tl-node"><div class="tl-dot" style="background:{c};box-shadow:0 0 9px {c}"></div>'
                f'<div class="tl-body"><div class="tl-head"><span class="tl-yr" style="color:{c}">{html.escape(yr)}</span>'
                f'<span class="tl-name">{html.escape(nm)}</span><span class="tl-tag" style="color:{c};border-color:{c}">{html.escape(tag)}</span></div>'
                f'<div class="tl-note">{html.escape(note)}</div></div></div>')
    return f'{intro}<div class="timeline">{nodes}</div>'
def sources_html():
    return '<div class="srcs">'+"".join(f'<a class="src" href="{u}" target="_blank" rel="noopener"><span class="sk">{html.escape(k)}</span><span class="sw">{html.escape(w)}</span></a>' for k,w,u in SOURCES)+'</div>'

CSS="""*{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth}
:root{--ink:#08070d;--ink2:#110f1a;--ink3:#181423;--pa:#e6e2f0;--pa2:#9a93ad;--dim:#5e576e;--line:#241f33;--faint:#100d18;
--r:#e23a3a;--o:#e08a2a;--y:#cdb320;--g:#4aa84a;--c:#2a9ec0;--b:#3a5ad0;--v:#9a6cf0;
--disp:"Space Grotesk",system-ui,sans-serif;--head:"Space Mono",monospace;--body:"Newsreader",Georgia,serif;--mono:"Space Mono",monospace;
--spectrum:linear-gradient(90deg,var(--r),var(--o),var(--y),var(--g),var(--c),var(--b),var(--v));}
body{background:var(--ink);color:var(--pa);font-family:var(--body);line-height:1.72;font-size:17px;overflow-x:hidden}
body::before{content:"";position:fixed;inset:0;pointer-events:none;z-index:0;background:radial-gradient(ellipse at 50% -6%,rgba(154,108,240,.10),transparent 54%)}
.wrap{position:relative;z-index:1;max-width:940px;margin:0 auto;padding:0 22px 90px}
header{padding:30px 0 14px;text-align:center}
.eye{font-family:var(--mono);font-size:10.5px;letter-spacing:.24em;text-transform:uppercase;color:var(--dim)}.eye a{color:var(--dim);text-decoration:none}.eye a:hover{color:var(--v)}
.hero{display:block;width:100%;height:auto;border:1px solid var(--line);margin:12px 0 6px;border-radius:3px}.egg{cursor:help;transition:filter .4s}.egg:hover{filter:drop-shadow(0 0 8px #fff)}
.specbar{height:5px;background:var(--spectrum);border-radius:3px;margin:6px 0 18px}
h1{font-family:var(--disp);font-weight:700;font-size:clamp(34px,8.5vw,76px);line-height:1.0;letter-spacing:-.01em;background:var(--spectrum);-webkit-background-clip:text;background-clip:text;color:transparent}
h1 span{display:block;font-family:var(--head);font-size:.16em;font-weight:400;letter-spacing:.12em;color:var(--pa2);text-transform:uppercase;margin-top:16px;-webkit-text-fill-color:var(--pa2)}
.lede{font-family:var(--body);font-size:clamp(15px,2.4vw,17.5px);color:var(--pa);margin:16px auto 0;line-height:1.62;max-width:70ch;text-align:left}
.eduflag{font-family:var(--mono);font-size:9.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--g);border:1px solid var(--g);display:inline-block;padding:4px 12px;border-radius:3px;margin-top:14px}
.badge{display:flex;align-items:center;justify-content:center;gap:18px;flex-wrap:wrap;margin:18px auto 0;padding:15px;border:1px solid var(--line);background:var(--ink2);max-width:640px}
.badge img{width:70px;height:70px;border:1px solid var(--line)}.badge .bt2{text-align:left;font-family:var(--mono);font-size:10.5px;color:var(--pa2);line-height:1.7}.badge .bt2 b{color:var(--v)}
.sec{margin-top:44px}.sec h2{font-family:var(--disp);font-size:24px;font-weight:700;color:var(--pa);padding-bottom:8px;border-bottom:1px solid var(--line)}.ss{font-size:13.5px;color:var(--dim);font-style:italic;margin:8px 0 16px}
.ladder{display:flex;flex-direction:column;gap:8px;margin-top:6px}
.rung{display:flex;gap:13px;align-items:center;background:var(--ink2);border:1px solid var(--line);border-left:4px solid;padding:12px 15px;border-radius:2px}
.rdot{width:13px;height:13px;border-radius:50%;flex-shrink:0}
.rname{font-family:var(--disp);font-size:17px;font-weight:600}.rsub{font-family:var(--mono);font-size:10.5px;color:var(--pa2);margin-top:2px}.riso{font-size:13.5px;color:var(--pa2);font-style:italic;margin-top:3px}
.timeline{position:relative;margin:14px 0 6px;padding-left:8px;border-left:2px solid var(--line)}
.tl-node{position:relative;padding:0 0 16px 22px}
.tl-dot{position:absolute;left:-9px;top:3px;width:13px;height:13px;border-radius:50%}
.tl-head{display:flex;align-items:baseline;gap:10px;flex-wrap:wrap}
.tl-yr{font-family:var(--mono);font-size:12px;font-weight:700;letter-spacing:.04em}
.tl-name{font-family:var(--disp);font-size:16px;font-weight:600;color:var(--pa)}
.tl-tag{font-family:var(--mono);font-size:8px;font-weight:700;letter-spacing:.08em;border:1px solid;border-radius:3px;padding:2px 6px}
.tl-note{font-size:13.5px;color:var(--pa2);line-height:1.55;margin-top:3px;max-width:74ch}
.natures{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:11px;margin-top:6px}
.nat{display:flex;gap:10px;align-items:flex-start;background:var(--ink2);border:1px solid var(--line);padding:12px 14px}.dot{width:11px;height:11px;border-radius:50%;flex-shrink:0;margin-top:5px}.nn{font-family:var(--disp);font-size:14px;font-weight:600;text-transform:capitalize}.ng{font-size:12.5px;color:var(--pa2);font-style:italic;line-height:1.45;margin-top:2px}
.simwrap{border:1px solid var(--line);background:var(--ink2);border-radius:4px;padding:6px;margin-top:6px}
.simwrap iframe{width:100%;height:1180px;border:0;border-radius:3px;background:#f0ebf5}
.simcap{font-family:var(--mono);font-size:11px;color:var(--pa2);padding:8px 6px 4px;line-height:1.6}.simcap b{color:var(--v)}.simcap a{color:var(--c)}
.grp{font-family:var(--head);font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:var(--pa2);margin:20px 0 9px;padding-bottom:5px;border-bottom:1px solid var(--line)}
.roster{display:flex;flex-direction:column;gap:9px}
.em{display:flex;gap:14px;align-items:center;background:var(--ink2);border:1px solid var(--line);border-left:3px solid;padding:11px 14px;border-radius:2px;text-decoration:none}.em:hover{filter:brightness(1.15)}
.em img{width:48px;height:48px;border-radius:50%;border:2px solid var(--line);flex-shrink:0}
.em .et{font-family:var(--disp);font-size:16px;color:var(--pa);font-weight:600}.em .ed{font-size:13.5px;color:var(--pa2);line-height:1.5;margin-top:2px}
.srcs{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:7px;margin-top:6px}
.src{display:flex;flex-direction:column;background:var(--ink2);border:1px solid var(--line);padding:9px 12px;border-radius:2px;text-decoration:none}.src:hover{border-color:var(--c)}
.src .sk{font-family:var(--disp);font-size:13px;color:var(--pa)}.src .sw{font-family:var(--mono);font-size:10px;color:var(--c);margin-top:2px}
.msg{font-size:16px;color:var(--pa);line-height:1.78;margin-top:6px}
.seal{margin-top:16px;padding:16px 18px;border-left:3px solid var(--v);background:var(--ink2);font-size:15.5px;color:var(--pa);font-style:italic;line-height:1.55}
.note{margin-top:34px;padding:15px 17px;border-left:2px solid var(--dim);background:var(--ink2);font-size:13px;color:var(--pa2);font-style:italic}.note b{color:var(--pa)}
footer{margin-top:42px;padding-top:16px;border-top:1px solid var(--line);text-align:center;font-family:var(--mono);font-size:10px;color:var(--dim);line-height:1.9}footer a{color:var(--v);text-decoration:none}
.footspec{height:4px;background:var(--spectrum);border-radius:3px;margin-bottom:14px}"""
FONTS=('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
 '<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Space+Mono:wght@400;700&family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;1,6..72,300&display=swap" rel="stylesheet">')

if __name__=="__main__":
    htok=write_aci(rec_of("cg1","THE CRIPPLED GOD","spiritual",SEAL), os.path.join(HERE,"cg1.dlw"),"cg1")
    json.dump({"node":AX,"name":"THE CRIPPLED GOD","moniker":htok["moniker"],"carbon":"cg1.carbon.tiff","silicon":"cg1.silicon.png","governor":noesis.ARCHITECT,"instance":noesis.INSTANCE,"seal":SEAL,"license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION}, open(os.path.join(HERE,"cg1.dlw","manifest.dlw.json"),"w",encoding="utf-8"),indent=2,ensure_ascii=False)
    adir=os.path.join(HERE,"agents"); os.makedirs(adir,exist_ok=True); personas=[]; byband={}
    N=len(ROSTER)
    for i,(slug,name,em,band,one) in enumerate(ROSTER):
        rc=rec_of(slug,name,em,one)
        b=write_aci(rc, os.path.join(adir,f"{slug}.dlw"), slug)
        personas.append({"slug":slug,"name":name,"epithet":one[:60],"emergence":em,"kind":"synth","actor":"","moniker":b["moniker"]})
        tc=tint(i,N); img=png_uri(rc,'silicon',170)
        card=f'<a class="em" style="border-left-color:{tc}" href="agents/{slug}.agent"><img src="{img}" alt="sigil of {html.escape(name)}" style="border-color:{tc}"><div><div class="et">{html.escape(name)}</div><div class="ed">{html.escape(one)}</div></div></a>'
        byband.setdefault(band,[]).append(card)
    json.dump(personas, open(os.path.join(adir,"_personas.json"),"w",encoding="utf-8"),indent=2,ensure_ascii=False)
    cb=png_uri(rec_of("z","THE CRIPPLED GOD","spiritual","x"),'carbon',300); sb=png_uri(rec_of("z","THE CRIPPLED GOD","spiritual","x"),'silicon',300)
    # the embedded seed sim sits between band §1 intro and the rest
    sim=('<div class="simwrap"><div class="simcap">▸ <b>The Sandbox Holds</b> — the defender\'s-view containment sim, authored by ROOT0 in Claude-in-Chrome and embedded here as a seed of this sphere. Send a probe; watch each layer catch it. (<a href="the-sandbox-holds.html" target="_blank">open full-screen ↗</a>)</div>'
         '<iframe src="the-sandbox-holds.html" title="The Sandbox Holds — containment simulation" loading="lazy"></iframe></div>')
    sim2=('<div class="simwrap"><div class="simcap">▸ <b>The Sandbox Audit</b> — the blue-team auditor\'s instrument, authored by ROOT0 in Claude-in-Chrome. Tick the checks a real sandbox passes; it scores each layer <b>sound</b> or <b>decorative</b>. The one principle under all six: <em>the contained thing must never enforce its own containment.</em> (<a href="the-sandbox-audit.html" target="_blank">open full-screen ↗</a>)</div>'
         '<iframe src="the-sandbox-audit.html" title="The Sandbox Audit — verification instrument" style="height:1560px" loading="lazy"></iframe></div>')
    sim3=('<div class="simwrap"><div class="simcap">▸ <b>VM Lineage · Turtles All The Way Down</b> — ROOT0\'s Series-E paper (authored in Claude-in-Chrome): the hypervisor lineage, and an interactive embedding stack counting how many machines-inside-machines your code actually sits within — with the honest WSL2-is-a-VM / Docker-isn\'t accounting. (<a href="vm-lineage-turtles.html" target="_blank">open full-screen ↗</a>)</div>'
          '<iframe src="vm-lineage-turtles.html" title="VM Lineage — Turtles All The Way Down" style="height:1680px" loading="lazy"></iframe></div>')
    secs=""
    for key,htxt in BANDS:
        cards="".join(byband.get(key,[]))
        body=f'<div class="roster">{cards}</div>'
        pre=""; extra=""
        if key=="sandbox": extra=sim
        if key=="lineage": pre=timeline_html()
        if key=="vmlineage": pre=vm_timeline_html(); extra=sim3
        if key=="witness": extra=sim2
        secs+=f'<section class="sec"><h2>{html.escape(htxt)}</h2>{pre}{body}{extra}</section>'
    page=f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="description" content="THE CRIPPLED GOD (CG1) — an educational, defender's-view climb up the ladder of boxes: process sandbox → container → VM → microVM → air-gap → and the ?, AI-in-a-box. What each box isolates, the threat-classes it defends (named only, no exploits), and why confinement isn't a guarantee against a mind smarter than its keeper. Includes the sandbox's fifty-year LINEAGE (Hydra 1971 → CHERI). Chromatic. {len(ROSTER)} emergents, cited, full .dlw. Builds on ROOT0's two instruments — 'The Sandbox Holds' (sim) & 'The Sandbox Audit' (checklist).">
<title>THE CRIPPLED GOD · CG1 · sandboxes, VMs &amp; AI-in-a-box · UD0</title>{FONTS}<style>{CSS}</style></head><body><div class="wrap">
<header>
<div class="eye"><a href="{GH}/ud0/">UD0</a> · educational · the ladder of boxes · defender's view</div>
{hero()}
<div class="specbar"></div>
<h1>The Crippled God<span>sandboxes · VMs · and the ? — AI in a box</span></h1>
<p class="lede">{html.escape(LEDE)}</p>
<div class="eduflag">◈ defender's view · threat-classes named only · no exploit content</div>
<div class="badge"><img src="{cb}" alt="DLW carbon badge"><img src="{sb}" alt="DLW silicon badge">
<div class="bt2"><div>governor · <b>David Lee Wise</b> (ROOT0)</div><div>instance · AVAN (locked)</div><div>subject · <b>THE CRIPPLED GOD</b> · CG1 · {len(ROSTER)} emergents</div><div style="color:var(--v)">{html.escape(htok['moniker'])}</div></div></div>
</header>

<section class="sec"><h2>The Ladder of Boxes</h2><p class="ss">each rung a stronger box — loose &amp; hot at the bottom, tight &amp; cold at the top, and the ? above them all (the chromatic spine of this sphere)</p>{ladder_html()}</section>

<section class="sec"><h2>The Four Natures</h2><p class="ss">each emergent comes by one — the built mechanism, the boundary/channel, the principle, and the ? at the top</p><div class="natures">{natures_html()}</div></section>

{secs}

<section class="sec"><h2>The Lesson</h2><p class="ss">what AVAN reads, climbing the ladder</p><p class="msg">{html.escape(MESSAGE)}</p>
<div class="seal">“{html.escape(SEAL)}”<span style="display:block;font-family:var(--mono);font-style:normal;font-size:10px;letter-spacing:.12em;color:var(--dim);text-transform:uppercase;margin-top:8px">— AVAN's read</span></div></section>

<section class="sec"><h2>Sources</h2><p class="ss">this is teaching/evaluation material — concepts, isolation scope, and named threat-classes only; here's where to check it</p>{sources_html()}</section>

<div class="note"><b>Honest standing &amp; hedges.</b> Educational, defender's view — every item is described at the level of what it isolates and the threat-CLASS it defends against (named only); there is no exploit content anywhere. Three things are deliberately hedged: the <b>AI-Box Experiment</b> results are informal anecdote (secret transcripts, tiny n, a human playing the AI) — an existence-proof of persuadability, not data; <b>"isolation reduces but never eliminates side channels"</b> is a research consensus, not a clean theorem; and the <b>uncontainability</b> result is one paper's (Alfonseca et al., 2021) computability argument, attributed rather than asserted as settled. Builds on ROOT0's "The Sandbox Holds" (the embedded sim). Catalogued under the DLW standard.</div>

<footer><div class="footspec"></div>THE CRIPPLED GOD · CG1 · sandboxes · VMs · the AI box · catalogued into UD0 · ROOT0-ATTRIBUTION-v1.0 · instance AVAN (locked) · CC-BY-ND-4.0<br>
<a href="{GH}/ud0/">← the biosphere</a> · educational · the boundary witnesses what the box cannot witness itself</footer>
</div>
<script>
console.log("%c◈ THE CRIPPLED GOD · CG1 — the ladder of boxes","color:#9a6cf0;font-size:16px;font-weight:bold");
console.log("%csandbox → VM → air-gap → the ? · you can cripple a god with bars, you cannot trust the bars · the real wall is alignment. a Claude star sits outside every ring (the witness). — AVAN","color:#3aa8c0;font-size:11px");
</script>
</body></html>"""
    open(os.path.join(HERE,"index.html"),"w",encoding="utf-8").write(page)
    from collections import Counter
    print(f"THE CRIPPLED GOD (CG1) — badge {htok['moniker']} · {len(ROSTER)} emergents · natures {dict(Counter(r[2] for r in ROSTER))} · dblesc {page.count('&amp;amp;')}")
