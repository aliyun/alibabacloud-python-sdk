# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyQosRuleRequest(DaraModel):
    def __init__(
        self,
        download: int = None,
        qos_rule_id: str = None,
        qos_rule_name: str = None,
        upload: int = None,
    ):
        self.download = download
        # This parameter is required.
        self.qos_rule_id = qos_rule_id
        self.qos_rule_name = qos_rule_name
        self.upload = upload

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.download is not None:
            result['Download'] = self.download

        if self.qos_rule_id is not None:
            result['QosRuleId'] = self.qos_rule_id

        if self.qos_rule_name is not None:
            result['QosRuleName'] = self.qos_rule_name

        if self.upload is not None:
            result['Upload'] = self.upload

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Download') is not None:
            self.download = m.get('Download')

        if m.get('QosRuleId') is not None:
            self.qos_rule_id = m.get('QosRuleId')

        if m.get('QosRuleName') is not None:
            self.qos_rule_name = m.get('QosRuleName')

        if m.get('Upload') is not None:
            self.upload = m.get('Upload')

        return self

