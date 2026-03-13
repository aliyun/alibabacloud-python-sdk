# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TriggerPlaybookRequest(DaraModel):
    def __init__(
        self,
        input_param: str = None,
        playbook_uuid: str = None,
    ):
        # The input parameters of the playbook.
        # 
        # This parameter is required.
        self.input_param = input_param
        # The playbook UUID.
        # 
        # >  You can call the [DescribePlaybooks](~~DescribePlaybooks~~) operation to query the playbook UUID.
        # 
        # This parameter is required.
        self.playbook_uuid = playbook_uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input_param is not None:
            result['InputParam'] = self.input_param

        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InputParam') is not None:
            self.input_param = m.get('InputParam')

        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')

        return self

