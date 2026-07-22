# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifySlsDispatchConfigRequest(DaraModel):
    def __init__(
        self,
        detail_config: str = None,
        log_version: int = None,
        modify_type: str = None,
    ):
        # The detailed configuration to modify.
        # <details>
        # <summary>Format for version 1</summary>
        # {"global":{"slsRegionId":"ap-southeast-1","logTime":180,"logStorage":1000}}
        # </details>
        # 
        # <details>
        # <summary>Format for version 2</summary>
        # {"cn":{"slsRegionId":"ap-southeast-1","logTime":180,"logStorage":3000},"intl":{"slsRegionId":"ap-southeast-1","logTime":180,"logStorage":2000}}
        # </details>
        # The fields are described as follows:
        # 
        # - slsRegionId: The region ID to which logs are delivered.
        # - logTime: The storage duration of logs. Unit: days.
        # - logStorage: The log storage capacity. Unit: GB. The total capacity specified must not exceed the total capacity purchased by the user.
        self.detail_config = detail_config
        # The log version. A value of 1 indicates one Logstore. A value of 2 indicates two Logstores.
        # 
        # 
        # >Notice: If ModifyType is set to version, set LogVersion to the target version. If ModifyType is set to config, set LogVersion to the current version of the user.
        self.log_version = log_version
        # The modification type. Valid values:
        # 
        # - version: The version is changed. For example, the version is changed from 1 (logs are delivered to one Logstore) to 2 (logs are delivered to two Logstores).
        # 
        # - config: The configuration is changed. For example, the log delivery region or the storage duration of logs is modified.
        self.modify_type = modify_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.detail_config is not None:
            result['DetailConfig'] = self.detail_config

        if self.log_version is not None:
            result['LogVersion'] = self.log_version

        if self.modify_type is not None:
            result['ModifyType'] = self.modify_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DetailConfig') is not None:
            self.detail_config = m.get('DetailConfig')

        if m.get('LogVersion') is not None:
            self.log_version = m.get('LogVersion')

        if m.get('ModifyType') is not None:
            self.modify_type = m.get('ModifyType')

        return self

