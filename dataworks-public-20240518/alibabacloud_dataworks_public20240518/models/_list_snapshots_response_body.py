# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class ListSnapshotsResponseBody(DaraModel):
    def __init__(
        self,
        paging_info: main_models.ListSnapshotsResponseBodyPagingInfo = None,
        request_id: str = None,
    ):
        # The pagination information.
        self.paging_info = paging_info
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.paging_info:
            self.paging_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.paging_info is not None:
            result['PagingInfo'] = self.paging_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PagingInfo') is not None:
            temp_model = main_models.ListSnapshotsResponseBodyPagingInfo()
            self.paging_info = temp_model.from_map(m.get('PagingInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListSnapshotsResponseBodyPagingInfo(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        snapshots: List[main_models.ListSnapshotsResponseBodyPagingInfoSnapshots] = None,
        total_count: int = None,
    ):
        # The page number.
        self.page_number = page_number
        # The page size.
        self.page_size = page_size
        # The list of snapshots.
        self.snapshots = snapshots
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.snapshots:
            for v1 in self.snapshots:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['Snapshots'] = []
        if self.snapshots is not None:
            for k1 in self.snapshots:
                result['Snapshots'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.snapshots = []
        if m.get('Snapshots') is not None:
            for k1 in m.get('Snapshots'):
                temp_model = main_models.ListSnapshotsResponseBodyPagingInfoSnapshots()
                self.snapshots.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListSnapshotsResponseBodyPagingInfoSnapshots(DaraModel):
    def __init__(
        self,
        comment: str = None,
        create_time: int = None,
        creator: str = None,
        id: str = None,
        namespace: str = None,
        object_id: str = None,
        type: str = None,
        version: int = None,
    ):
        # The snapshot comment.
        self.comment = comment
        # The snapshot creation time, in millisecond UNIX timestamp.
        self.create_time = create_time
        # The employee ID of the submitter.
        self.creator = creator
        # The unique ID of the snapshot.
        self.id = id
        # The namespace.
        self.namespace = namespace
        # The unique ID of the object to which the snapshot belongs.
        self.object_id = object_id
        # The snapshot type.
        self.type = type
        # The version number.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.id is not None:
            result['Id'] = self.id

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.object_id is not None:
            result['ObjectId'] = self.object_id

        if self.type is not None:
            result['Type'] = self.type

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

