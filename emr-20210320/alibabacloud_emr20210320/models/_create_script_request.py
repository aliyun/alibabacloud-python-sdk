# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr20210320 import models as main_models
from darabonba.model import DaraModel

class CreateScriptRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        region_id: str = None,
        script_type: str = None,
        scripts: List[main_models.Script] = None,
        timeout_secs: str = None,
    ):
        # The cluster ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The script type. Valid values:
        # 
        # - BOOTSTRAP: an ECS instance bootstrap script.
        # 
        # - NORMAL: a normal script.
        # 
        # This parameter is required.
        self.script_type = script_type
        # The list of scripts.
        # 
        # This parameter is required.
        self.scripts = scripts
        # The timeout period for manually executing the script. This parameter is not supported for bootstrap scripts.
        self.timeout_secs = timeout_secs

    def validate(self):
        if self.scripts:
            for v1 in self.scripts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.script_type is not None:
            result['ScriptType'] = self.script_type

        result['Scripts'] = []
        if self.scripts is not None:
            for k1 in self.scripts:
                result['Scripts'].append(k1.to_map() if k1 else None)

        if self.timeout_secs is not None:
            result['TimeoutSecs'] = self.timeout_secs

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ScriptType') is not None:
            self.script_type = m.get('ScriptType')

        self.scripts = []
        if m.get('Scripts') is not None:
            for k1 in m.get('Scripts'):
                temp_model = main_models.Script()
                self.scripts.append(temp_model.from_map(k1))

        if m.get('TimeoutSecs') is not None:
            self.timeout_secs = m.get('TimeoutSecs')

        return self

