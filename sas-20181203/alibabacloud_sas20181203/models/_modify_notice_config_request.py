# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyNoticeConfigRequest(DaraModel):
    def __init__(
        self,
        biz_type: str = None,
        focus_level: str = None,
        project: str = None,
        route: int = None,
        source_ip: str = None,
        time_limit: int = None,
    ):
        # The notification configuration type. By default, notifications are sent by SMS, email, or internal message. Valid values:
        # 
        # - **cms**: CloudMonitor push.
        self.biz_type = biz_type
        # The focus level. Separate multiple levels with commas (,).
        # 
        # When **Project** is **yundun_soar_incident_generate** or **yundun_soar_incident_update**, valid values:
        # 
        # - **CRITICAL**: Critical.
        # - **HIGH**: High-risk.
        # - **MEDIUM**: Medium-risk.
        # - **LOW**: Low-risk.
        # - **INFO**: Informational.
        # 
        # When **Project** is **yundun_sas_antiransomware_task**, valid values:
        # 
        # - **Success**: Execution succeeded.
        # - **Failed**: Execution failed.
        self.focus_level = focus_level
        # ### Project identity
        # 
        # #### When the BizType field is empty: valid values
        # - **yundun_security_Weekreport**: Security weekly report (email only)
        # - **sas_healthcheck**: Baseline check
        # - **yundun_defennce_antiRansomware_overflow**: Anti-ransomware storage space exceeded
        # - **yundun_sas_cloudsiem_log**: Cloud Threat Detection and Response (CTDR) log excess notification
        # - **sas_suspicious**: Security alert
        # - **yundun_aegis_AV_true**: Precise defense
        # - **yundun_sas_ak_leakage AccessKey**: AccessKey leak intelligence
        # - **yundun_sas_config_alert**: Cloud platform configuration check
        # - **yundun_sas_vul_Emergency**: Emergency vulnerability intelligence
        # - **yundun_webguard_event**: Web tamper-proofing
        # - **yundun_sas_cloud_native_firewall**: Container firewall anomaly alert notification (email only)
        # - **yundun_sas_cloud_native_firewall_Defense**: Container firewall active defense notification (email only)
        # - **yundun_IP_Blocking**: Malicious IP blocking alerting notification
        # - **yundun_sas_anti_virus_config**: Virus scan notification
        # - **yundun_sas_log**: Log storage exceeded
        # - **yundun_honeypot_alarm**: Cloud honeypot alerting
        # - **aliyun_rasp_alarm**: Application protection alerting
        # - **yundun_soar_incident_generate**: New security incident
        # - **yundun_soar_incident_update**: Updated security incident
        # > **yundun_security_Weekreport** sends a weekly report to notify you of unresolved vulnerabilities.
        # 
        # ---
        # 
        # #### When the BizType field is `cms`: valid values
        # - **Vul_event**: Vulnerability result details
        # - **Hc_summary**: Baseline check result summary
        # - **Cspm_summary**: Cloud Security Posture Management (CSPM) result summary
        # - **Vul_summary**: Vulnerability result summary
        # - **Agentless_event**: Agentless detection result details
        # - **Filedetect_event**: Malicious file SDK result details
        # - **Rasp_event**: Application protection result details.
        self.project = project
        # ### Notification method
        # 
        # #### When BizType is empty
        # - 0: disabled
        # - 1: SMS enabled
        # - 2: email enabled
        # - 4: internal message enabled
        # - 3: SMS and email enabled
        # - 5: SMS and internal message enabled
        # - 6: email and internal message enabled
        # - 7: SMS, email, and internal message all enabled
        # 
        # #### When BizType is `cms`
        # - 0: CloudMonitor push disabled
        # - 1: CloudMonitor push enabled.
        self.route = route
        # The IP address of the access source.
        self.source_ip = source_ip
        # ### Notification time limit
        # 
        # #### When the BizType field is empty: valid values
        # - **0**: No limit.
        # - **1**: Notifications are sent only between 08:00 and 22:00.
        # 
        # #### When the BizType field is `cms`
        # Specifies the push frequency limit, in seconds. The minimum value is **60**.
        self.time_limit = time_limit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.focus_level is not None:
            result['FocusLevel'] = self.focus_level

        if self.project is not None:
            result['Project'] = self.project

        if self.route is not None:
            result['Route'] = self.route

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.time_limit is not None:
            result['TimeLimit'] = self.time_limit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('FocusLevel') is not None:
            self.focus_level = m.get('FocusLevel')

        if m.get('Project') is not None:
            self.project = m.get('Project')

        if m.get('Route') is not None:
            self.route = m.get('Route')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('TimeLimit') is not None:
            self.time_limit = m.get('TimeLimit')

        return self

