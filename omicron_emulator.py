import json
import time
import random

# ----------------------------
# Omicron Emulator – Super Cheat-Sheet Simulator
# ----------------------------

class OmicronEmulator:
    def __init__(self):
        self.variables = {}
        self.modules = {}
        self.audit_logs = []
        self.devices = []
        self.honeypots = []

    # ------------------------
    # Basic OPL commands
    # ------------------------
    def output(self, value):
        print(f"[OUTPUT] {value}")
        return value

    def let(self, var, value):
        self.variables[var] = value
        return value

    def get_var(self, var):
        return self.variables.get(var, None)

    def cast(self, value, type_):
        if type_ == "int":
            return int(value)
        elif type_ == "float":
            return float(value)
        elif type_ == "str":
            return str(value)
        elif type_ == "bool":
            return bool(value)
        return value

    # ------------------------
    # Modules Simulation
    # ------------------------
    def use_module(self, name):
        self.modules[name] = True
        print(f"[MODULE LOADED] {name}")

    def audit_log(self, tag, info):
        self.audit_logs.append((tag, info))
        print(f"[AUDIT] {tag} -> {info}")

    def spawn_device(self, type_):
        dev = {"type": type_, "id": f"{type_}_{len(self.devices)+1}"}
        self.devices.append(dev)
        print(f"[DEVICE SPAWNED] {dev}")
        return dev

    def honeypot_spawn(self, name):
        hp = {"name": name, "interactions": []}
        self.honeypots.append(hp)
        print(f"[HONEYPOT CREATED] {hp}")
        return hp

    def honeypot_collect(self, hp):
        hp["interactions"].append(f"attacker_{random.randint(1,100)}")
        print(f"[HONEYPOT COLLECT] {hp['name']} -> interactions updated")

    def lab_traffic_play(self, profile):
        print(f"[LAB TRAFFIC] Running profile: {profile}")

    def mirror_attach(self, iface):
        print(f"[MIRROR] Attached to interface: {iface}")

    def mirror_playback(self, window="1h"):
        print(f"[MIRROR PLAYBACK] Last {window} of traffic replayed")

    # ------------------------
    # Examples of Feature Commands
    # ------------------------
    def fake_cctv_honeypot(self):
        self.use_module("sentinel.lab")
        self.use_module("echo.hone")
        self.use_module("oblivion.audit")
        cam = self.spawn_device("camera:v1")
        self.lab_traffic_play("baseline")
        h = self.honeypot_spawn("fake-cam")
        self.honeypot_collect(h)
        self.audit_log("honeypot-cam", h)
        self.output("Fake CCTV Honeypot Running")

    def passive_network_scan(self):
        self.use_module("void.net")
        devices = [{"ip": f"10.10.0.{i}"} for i in range(1,6)]
        self.audit_log("net-discover", devices)
        self.output(f"Passive Network Scan Complete: {devices}")

    def hybrid_encryption_demo(self):
        self.use_module("abyss.crypto")
        env = f"sealed_{random.randint(1000,9999)}"
        self.audit_log("sealed", env)
        self.output(f"Hybrid Encryption Demo Complete: {env}")

    # ------------------------
    # Run Example Lab
    # ------------------------
    def full_honeypot_lab(self):
        cam = self.spawn_device("camera:v1")
        r = self.spawn_device("router:v2")
        bulb = self.spawn_device("iot-bulb:v1")
        self.lab_traffic_play("baseline")
        hc = self.honeypot_spawn("fake-cam")
        hr = self.honeypot_spawn("fake-router")
        hb = self.honeypot_spawn("fake-bulb")
        self.honeypot_collect(hc)
        self.honeypot_collect(hr)
        self.honeypot_collect(hb)
        self.mirror_attach("eth0")
        self.mirror_playback("30m")
        self.audit_log("honeypot-lab", [hc, hr, hb])
        self.output("Full Honeypot Lab Running")

# ----------------------------
# Main Emulator CLI
# ----------------------------
if __name__ == "__main__":
    om = OmicronEmulator()
    print("\n=== Omicron Emulator Loaded ===\n")
    print("Available Commands:")
    print("1. om.fake_cctv_honeypot()")
    print("2. om.passive_network_scan()")
    print("3. om.hybrid_encryption_demo()")
    print("4. om.full_honeypot_lab()")
    print("\nVariables accessible via om.variables\n")

    # Simple CLI loop
    while True:
        cmd = input("Omicron> ")
        if cmd in ["exit", "quit"]:
            print("Exiting Omicron Emulator...")
            break
        try:
            exec(f"om.{cmd}")
        except Exception as e:
            print(f"[ERROR] {e}")
