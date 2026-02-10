# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeSuspiciousOverallConfigResponseBody(DaraModel):
    def __init__(
        self,
        overall_config: main_models.DescribeSuspiciousOverallConfigResponseBodyOverallConfig = None,
        request_id: str = None,
    ):
        # The configuration.
        self.overall_config = overall_config
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.overall_config:
            self.overall_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.overall_config is not None:
            result['OverallConfig'] = self.overall_config.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OverallConfig') is not None:
            temp_model = main_models.DescribeSuspiciousOverallConfigResponseBodyOverallConfig()
            self.overall_config = temp_model.from_map(m.get('OverallConfig'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeSuspiciousOverallConfigResponseBodyOverallConfig(DaraModel):
    def __init__(
        self,
        config: str = None,
        type: str = None,
    ):
        # The status of the feature. Valid values:
        # 
        # *   **off**: disabled
        # *   **on**: enabled
        self.config = config
        # The type of the feature. Valid values:
        # 
        # *   **auto_breaking**: Anti-Virus
        # *   **ransomware_breaking**: Anti-ransomware (Bait Capture)
        # *   **webshell_cloud_breaking**: Webshell Protection
        # *   **alinet**: Behavior prevention
        # *   **k8s_log_analysis**: K8s Threat Detection
        # *   **alisecguard**: Defense mode for Client Protection
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['Config'] = self.config

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

