cp monitor-manager-start.py /usr/local/bin/

chmod 644 MonitorManager.service
cp MonitorManager.service /lib/systemd/system/

systemctl daemon-reload
systemctl enable MonitorManager.service
