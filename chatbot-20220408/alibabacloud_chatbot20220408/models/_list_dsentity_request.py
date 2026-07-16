# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDSEntityRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        entity_type: str = None,
        instance_id: str = None,
        keyword: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The key of the business space. If this parameter is not set, the default business space is used. You can find this key on the Business Management page of your main account.
        self.agent_key = agent_key
        # The entity type. If you omit this parameter, all custom entities are returned.
        self.entity_type = entity_type
        # The robot ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # A keyword to filter entities by name using a \\"contains\\" match. Future releases will also support searching by entity member and synonym.
        self.keyword = keyword
        # The current page number. Default value: 1.
        self.page_number = page_number
        # The number of entries to return per page. The default value is 10.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key

        if self.entity_type is not None:
            result['EntityType'] = self.entity_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

