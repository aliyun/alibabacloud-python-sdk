# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePlaybooksRequest(DaraModel):
    def __init__(
        self,
        active: int = None,
        end_millis: int = None,
        lang: str = None,
        name: str = None,
        order: str = None,
        own_type: str = None,
        page_number: int = None,
        page_size: int = None,
        param_types: str = None,
        playbook_uuid: str = None,
        playbook_uuids: str = None,
        sort: int = None,
        start_millis: int = None,
    ):
        # The status of the playbook. Valid values:
        # 
        # - **1**: The playbook is enabled.
        # 
        # - **0**: The playbook is disabled.
        self.active = active
        # The end of the time range to query. This value is a 13-digit timestamp.
        self.end_millis = end_millis
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # - **zh**: Chinese.
        # 
        # - **en**: English.
        self.lang = lang
        # The name of the playbook.
        self.name = name
        # The sort order. Default value: **desc**. Valid values:
        # 
        # - **desc**: descending.
        # 
        # - **asc**: ascending.
        self.order = order
        # The type of the playbook. Valid values:
        # 
        # - **preset**: predefined playbook.
        # 
        # - **user**: custom playbook.
        self.own_type = own_type
        # The page number of the page to return. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page. Default value: 20. If you leave this parameter empty, 10 entries are returned by default.
        # 
        # > Specify a value for this parameter.
        self.page_size = page_size
        # The trigger type of the playbook. If you do not specify this parameter, playbooks of all trigger types are queried. Valid values:
        # 
        # - **template-incident**: security event.
        # 
        # - **template-ip**: IP entity.
        # 
        # - **template-file**: file entity.
        # 
        # - **template-process**: process entity.
        # 
        # - **template-alert**: security alert.
        # 
        # - **template-domain**: domain name entity.
        # 
        # - **template-container**: container entity.
        # 
        # - **template-host**: host entity.
        # 
        # - **template-custom**: custom.
        self.param_types = param_types
        # The UUID of the playbook.
        # 
        # > Call the [CreatePlaybook](~~CreatePlaybook~~) operation to obtain this parameter.
        self.playbook_uuid = playbook_uuid
        # A comma-separated list of playbook UUIDs. You can specify up to 100 UUIDs.
        self.playbook_uuids = playbook_uuids
        # The field to sort by. Default value: **1**. Valid values:
        # 
        # - **1**: last modification time.
        # 
        # - **2**: last running time.
        self.sort = sort
        # The start of the time range to query. This value is a 13-digit timestamp.
        self.start_millis = start_millis

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active is not None:
            result['Active'] = self.active

        if self.end_millis is not None:
            result['EndMillis'] = self.end_millis

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.name is not None:
            result['Name'] = self.name

        if self.order is not None:
            result['Order'] = self.order

        if self.own_type is not None:
            result['OwnType'] = self.own_type

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.param_types is not None:
            result['ParamTypes'] = self.param_types

        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid

        if self.playbook_uuids is not None:
            result['PlaybookUuids'] = self.playbook_uuids

        if self.sort is not None:
            result['Sort'] = self.sort

        if self.start_millis is not None:
            result['StartMillis'] = self.start_millis

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Active') is not None:
            self.active = m.get('Active')

        if m.get('EndMillis') is not None:
            self.end_millis = m.get('EndMillis')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('OwnType') is not None:
            self.own_type = m.get('OwnType')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ParamTypes') is not None:
            self.param_types = m.get('ParamTypes')

        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')

        if m.get('PlaybookUuids') is not None:
            self.playbook_uuids = m.get('PlaybookUuids')

        if m.get('Sort') is not None:
            self.sort = m.get('Sort')

        if m.get('StartMillis') is not None:
            self.start_millis = m.get('StartMillis')

        return self

