# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_emr20210320 import models as main_models
from darabonba.model import DaraModel

class UpdateScriptRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        region_id: str = None,
        script: main_models.Script = None,
        script_id: str = None,
        script_type: str = None,
    ):
        # The cluster ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The script.
        # 
        # This parameter is required.
        self.script = script
        # The script ID.
        # 
        # This parameter is required.
        self.script_id = script_id
        # The type of the script. Valid values:
        # 
        # *   BOOTSTRAP: indicates a bootstrap action of the Elastic Compute Service (ECS) instance.
        # *   NORMAL: indicates a common script.
        # 
        # This parameter is required.
        self.script_type = script_type

    def validate(self):
        if self.script:
            self.script.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.script is not None:
            result['Script'] = self.script.to_map()

        if self.script_id is not None:
            result['ScriptId'] = self.script_id

        if self.script_type is not None:
            result['ScriptType'] = self.script_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Script') is not None:
            temp_model = main_models.Script()
            self.script = temp_model.from_map(m.get('Script'))

        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')

        if m.get('ScriptType') is not None:
            self.script_type = m.get('ScriptType')

        return self

