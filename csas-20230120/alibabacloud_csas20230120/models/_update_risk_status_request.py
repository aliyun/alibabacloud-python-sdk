# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateRiskStatusRequest(DaraModel):
    def __init__(
        self,
        risk_confirm: str = None,
        risk_confirm_desc: str = None,
        risk_id: str = None,
        risk_scene: str = None,
        status: str = None,
    ):
        # The manually confirmed risk conclusion. This parameter is required when `Status` is set to `Processed`. Do not specify this parameter when `Status` is set to `Unprocess` or `Processing`. Valid values:
        # * `Risk`: Confirmed as risky.
        # * `Ignore`: Confirmed as not risky.
        # * `Invalid`: Confirmed as a false positive.
        self.risk_confirm = risk_confirm
        # The description of the risk event processing decision. The value must be 1 to 128 characters in length.
        self.risk_confirm_desc = risk_confirm_desc
        # The risk event ID. You can obtain the value from the following operation:
        # * `ListRiskItems`: Queries the list of risk events.
        self.risk_id = risk_id
        # The risk scenario. This parameter is optional. If not specified, the system automatically populates it based on RiskId. Valid values:
        # * account_share: Account sharing.
        # * account_stolen: Account stolen.
        # * device_share: Device sharing.
        # * remote_logon: Remote logon.
        # * sensitive_data_leakage: Sensitive data leakage.
        # * `compressed_archive_exfil`: Internal network data compression and exfiltration.
        # * lateral_scanning: Lateral scanning.
        # * ai_skill_malware: Malicious skill.
        # * ai_config_check: AI configuration check.
        # * openclaw_vulnerability: OpenClaw vulnerability.
        self.risk_scene = risk_scene
        # The processing status of the risk event. Valid values:
        # * `Unprocess`: Unprocessed.
        # * `Processing`: Being processed.
        # * `Processed`: Processed.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.risk_confirm is not None:
            result['RiskConfirm'] = self.risk_confirm

        if self.risk_confirm_desc is not None:
            result['RiskConfirmDesc'] = self.risk_confirm_desc

        if self.risk_id is not None:
            result['RiskId'] = self.risk_id

        if self.risk_scene is not None:
            result['RiskScene'] = self.risk_scene

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RiskConfirm') is not None:
            self.risk_confirm = m.get('RiskConfirm')

        if m.get('RiskConfirmDesc') is not None:
            self.risk_confirm_desc = m.get('RiskConfirmDesc')

        if m.get('RiskId') is not None:
            self.risk_id = m.get('RiskId')

        if m.get('RiskScene') is not None:
            self.risk_scene = m.get('RiskScene')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

