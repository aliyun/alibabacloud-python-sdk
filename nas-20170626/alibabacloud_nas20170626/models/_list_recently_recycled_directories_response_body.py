# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nas20170626 import models as main_models
from darabonba.model import DaraModel

class ListRecentlyRecycledDirectoriesResponseBody(DaraModel):
    def __init__(
        self,
        entries: List[main_models.ListRecentlyRecycledDirectoriesResponseBodyEntries] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The information about directories on which delete operations were recently performed.
        self.entries = entries
        # The pagination token for the next page.
        # 
        # If the query results are not completely returned, the NextToken parameter is returned with a value. You can specify the NextToken value in the next request to continue the query.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.entries:
            for v1 in self.entries:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Entries'] = []
        if self.entries is not None:
            for k1 in self.entries:
                result['Entries'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.entries = []
        if m.get('Entries') is not None:
            for k1 in m.get('Entries'):
                temp_model = main_models.ListRecentlyRecycledDirectoriesResponseBodyEntries()
                self.entries.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListRecentlyRecycledDirectoriesResponseBodyEntries(DaraModel):
    def __init__(
        self,
        file_id: str = None,
        last_delete_time: str = None,
        name: str = None,
        path: str = None,
    ):
        # The directory ID.
        self.file_id = file_id
        # The most recent time when a delete operation was performed on the directory. The time follows the ISO 8601 standard in UTC. Format: yyyy-MM-ddTHH:mm:ssZ.
        self.last_delete_time = last_delete_time
        # The name of the directory.
        self.name = name
        # The absolute path of the directory.
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.last_delete_time is not None:
            result['LastDeleteTime'] = self.last_delete_time

        if self.name is not None:
            result['Name'] = self.name

        if self.path is not None:
            result['Path'] = self.path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('LastDeleteTime') is not None:
            self.last_delete_time = m.get('LastDeleteTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        return self

