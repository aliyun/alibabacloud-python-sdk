# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListCertRequest(DaraModel):
    def __init__(
        self,
        after_date: str = None,
        before_date: str = None,
        current_page: int = None,
        instance_uuid: str = None,
        max_results: int = None,
        next_token: str = None,
        parent_identifier: str = None,
        show_size: int = None,
        status: str = None,
        type: str = None,
    ):
        self.after_date = after_date
        self.before_date = before_date
        self.current_page = current_page
        self.instance_uuid = instance_uuid
        self.max_results = max_results
        self.next_token = next_token
        self.parent_identifier = parent_identifier
        self.show_size = show_size
        self.status = status
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.after_date is not None:
            result['AfterDate'] = self.after_date

        if self.before_date is not None:
            result['BeforeDate'] = self.before_date

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.instance_uuid is not None:
            result['InstanceUuid'] = self.instance_uuid

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.parent_identifier is not None:
            result['ParentIdentifier'] = self.parent_identifier

        if self.show_size is not None:
            result['ShowSize'] = self.show_size

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AfterDate') is not None:
            self.after_date = m.get('AfterDate')

        if m.get('BeforeDate') is not None:
            self.before_date = m.get('BeforeDate')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('InstanceUuid') is not None:
            self.instance_uuid = m.get('InstanceUuid')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('ParentIdentifier') is not None:
            self.parent_identifier = m.get('ParentIdentifier')

        if m.get('ShowSize') is not None:
            self.show_size = m.get('ShowSize')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

