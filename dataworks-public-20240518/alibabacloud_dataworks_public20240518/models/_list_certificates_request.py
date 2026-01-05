# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListCertificatesRequest(DaraModel):
    def __init__(
        self,
        create_user: str = None,
        end_create_time: int = None,
        name: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        project_id: int = None,
        sort_by: str = None,
        start_create_time: int = None,
    ):
        # The ID of the user who created the certificate files.
        self.create_user = create_user
        # The time when the certificate file was created. You can call this operation to query the files that are created before the time. Unit: milliseconds.
        self.end_create_time = end_create_time
        # The name of the certificate file. Fuzzy match by file name is supported.
        self.name = name
        # The order in which you want to sort the certificate files. Valid values: Desc: descending order ASC: ascending order Default value: Asc
        self.order = order
        # The page number. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 10. Maximum value: 100.
        self.page_size = page_size
        # The ID of the workspace to which the certificate file belongs.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The field used to sort the certificate files. Valid values: CreateTime Id Name Default value: Id
        self.sort_by = sort_by
        # The time when the certificate file was created. You can call this operation to query the files that are created after the time. Unit: milliseconds.
        self.start_create_time = start_create_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_user is not None:
            result['CreateUser'] = self.create_user

        if self.end_create_time is not None:
            result['EndCreateTime'] = self.end_create_time

        if self.name is not None:
            result['Name'] = self.name

        if self.order is not None:
            result['Order'] = self.order

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.start_create_time is not None:
            result['StartCreateTime'] = self.start_create_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')

        if m.get('EndCreateTime') is not None:
            self.end_create_time = m.get('EndCreateTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('StartCreateTime') is not None:
            self.start_create_time = m.get('StartCreateTime')

        return self

