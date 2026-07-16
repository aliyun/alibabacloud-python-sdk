# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListScriptsRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        nlu_engine: str = None,
        page_number: int = None,
        page_size: int = None,
        script_name: str = None,
    ):
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The NLU engine.
        # 
        # - Leave this parameter empty to query scripts that use small models.
        # 
        # - Set this parameter to `Prompts` to query scripts that use the text completion mode of a large model.
        # 
        # - Set this parameter to `SSE_FUNCTION` to query scripts that use the function calling mode of a large model.
        # 
        # - Set this parameter to `BeeBot` to query scripts that use the workflow configuration mode of a large model.
        self.nlu_engine = nlu_engine
        # The page number.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The number of entries per page.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The name of the script.
        self.script_name = script_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.nlu_engine is not None:
            result['NluEngine'] = self.nlu_engine

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.script_name is not None:
            result['ScriptName'] = self.script_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NluEngine') is not None:
            self.nlu_engine = m.get('NluEngine')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ScriptName') is not None:
            self.script_name = m.get('ScriptName')

        return self

