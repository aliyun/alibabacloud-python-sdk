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
        # Activation status of the playbook. Values:
        # 
        # - **1**: Indicates the playbook is activated.
        # - **0**: Indicates the playbook is not activated.
        self.active = active
        # End time for the query, in 13-digit timestamp format.
        self.end_millis = end_millis
        # Specifies the language type for the request and response, default is **zh**. Values:
        # - **zh**: Chinese.
        # - **en**: English.
        self.lang = lang
        # The name of the playbook.
        self.name = name
        # The sorting logic, with a default value of **desc**. Values:
        # - **desc**: Descending order.
        # - **asc**: Ascending order.
        self.order = order
        # Type of the playbook. Values:
        # 
        # - **preset**: Predefined playbook.
        # - **user**: Custom playbook.
        self.own_type = own_type
        # Sets the page number from which to start displaying the query results. The default value is 1, indicating the first page.
        self.page_number = page_number
        # Specifies the maximum number of items to display per page in a paginated query. The default number of items per page is 20. If the PageSize parameter is empty, it will return 10 items by default.
        # > It is recommended that the PageSize value is not empty.
        self.page_size = page_size
        # The trigger method for the playbook, with a default value of **query all**. Values:
        # - **template-incident**: Security incident.
        # - **template-ip**: IP entity.
        # - **template-file**: File entity.
        # - **template-process**: Process entity.
        # - **template-alert**: Security alert.
        # - **template-domain**: Domain entity.
        # - **template-container**: Container entity.
        # - **template-host**: Host entity.
        # - **template-custom**: Custom.
        self.param_types = param_types
        # The UUID of the playbook.
        # > You can use the UUID to query specific playbook information.
        # > - Call the [CreatePlaybook](~~CreatePlaybook~~) API to obtain this parameter.
        self.playbook_uuid = playbook_uuid
        # UUID List of the playbook.
        # 
        # Note You can use the UUID list to query specific playbook information.
        # Call the DescribePlaybooks API to obtain this parameter.
        self.playbook_uuids = playbook_uuids
        # The sorting basis, with a default value of **1**. Values:
        # - **1**: Last modified time.
        # - **2**: Most recent execution time.
        self.sort = sort
        # Start time for the query, in 13-digit timestamp format.
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

