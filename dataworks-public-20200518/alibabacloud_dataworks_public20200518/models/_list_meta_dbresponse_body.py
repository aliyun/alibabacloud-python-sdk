# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class ListMetaDBResponseBody(DaraModel):
    def __init__(
        self,
        database_info: main_models.ListMetaDBResponseBodyDatabaseInfo = None,
        request_id: str = None,
    ):
        # The information about the metadatabases.
        self.database_info = database_info
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.database_info:
            self.database_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.database_info is not None:
            result['DatabaseInfo'] = self.database_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseInfo') is not None:
            temp_model = main_models.ListMetaDBResponseBodyDatabaseInfo()
            self.database_info = temp_model.from_map(m.get('DatabaseInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListMetaDBResponseBodyDatabaseInfo(DaraModel):
    def __init__(
        self,
        db_list: List[main_models.ListMetaDBResponseBodyDatabaseInfoDbList] = None,
        total_count: int = None,
    ):
        # The metadatabases.
        self.db_list = db_list
        # The total number of the metadatabases returned.
        self.total_count = total_count

    def validate(self):
        if self.db_list:
            for v1 in self.db_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DbList'] = []
        if self.db_list is not None:
            for k1 in self.db_list:
                result['DbList'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.db_list = []
        if m.get('DbList') is not None:
            for k1 in m.get('DbList'):
                temp_model = main_models.ListMetaDBResponseBodyDatabaseInfoDbList()
                self.db_list.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListMetaDBResponseBodyDatabaseInfoDbList(DaraModel):
    def __init__(
        self,
        create_time_stamp: int = None,
        location: str = None,
        modified_time_stamp: int = None,
        name: str = None,
        owner_id: str = None,
        type: str = None,
        uuid: str = None,
    ):
        # The timestamp at which the metadatabase was created. You can convert the timestamp to the date based on the time zone that you use.
        self.create_time_stamp = create_time_stamp
        # The URL of the metadatabase.
        self.location = location
        # The timestamp at which the metadatabase was updated.
        self.modified_time_stamp = modified_time_stamp
        # The name of the metadatabase.
        self.name = name
        # The owner ID.
        self.owner_id = owner_id
        # The type of the metadatabase.
        self.type = type
        # The UUID of the metadatabase.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time_stamp is not None:
            result['CreateTimeStamp'] = self.create_time_stamp

        if self.location is not None:
            result['Location'] = self.location

        if self.modified_time_stamp is not None:
            result['ModifiedTimeStamp'] = self.modified_time_stamp

        if self.name is not None:
            result['Name'] = self.name

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.type is not None:
            result['Type'] = self.type

        if self.uuid is not None:
            result['UUID'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTimeStamp') is not None:
            self.create_time_stamp = m.get('CreateTimeStamp')

        if m.get('Location') is not None:
            self.location = m.get('Location')

        if m.get('ModifiedTimeStamp') is not None:
            self.modified_time_stamp = m.get('ModifiedTimeStamp')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UUID') is not None:
            self.uuid = m.get('UUID')

        return self

