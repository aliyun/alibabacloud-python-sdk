# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nas20170626 import models as main_models
from darabonba.model import DaraModel

class DescribeDirQuotasResponseBody(DaraModel):
    def __init__(
        self,
        dir_quota_infos: List[main_models.DescribeDirQuotasResponseBodyDirQuotaInfos] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The queried directory quotas.
        self.dir_quota_infos = dir_quota_infos
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of directories.
        self.total_count = total_count

    def validate(self):
        if self.dir_quota_infos:
            for v1 in self.dir_quota_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DirQuotaInfos'] = []
        if self.dir_quota_infos is not None:
            for k1 in self.dir_quota_infos:
                result['DirQuotaInfos'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dir_quota_infos = []
        if m.get('DirQuotaInfos') is not None:
            for k1 in m.get('DirQuotaInfos'):
                temp_model = main_models.DescribeDirQuotasResponseBodyDirQuotaInfos()
                self.dir_quota_infos.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeDirQuotasResponseBodyDirQuotaInfos(DaraModel):
    def __init__(
        self,
        dir_inode: str = None,
        path: str = None,
        status: str = None,
        user_quota_infos: List[main_models.DescribeDirQuotasResponseBodyDirQuotaInfosUserQuotaInfos] = None,
    ):
        # The inode number of the directory.
        self.dir_inode = dir_inode
        # The absolute path of a directory.
        self.path = path
        # The status of the quota created for the directory. Valid values: Initializing and Normal. The Initializing state indicates that the quota is being created. The Normal state indicates that the quota is created.
        self.status = status
        # The information about quotas for all users.
        self.user_quota_infos = user_quota_infos

    def validate(self):
        if self.user_quota_infos:
            for v1 in self.user_quota_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dir_inode is not None:
            result['DirInode'] = self.dir_inode

        if self.path is not None:
            result['Path'] = self.path

        if self.status is not None:
            result['Status'] = self.status

        result['UserQuotaInfos'] = []
        if self.user_quota_infos is not None:
            for k1 in self.user_quota_infos:
                result['UserQuotaInfos'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirInode') is not None:
            self.dir_inode = m.get('DirInode')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.user_quota_infos = []
        if m.get('UserQuotaInfos') is not None:
            for k1 in m.get('UserQuotaInfos'):
                temp_model = main_models.DescribeDirQuotasResponseBodyDirQuotaInfosUserQuotaInfos()
                self.user_quota_infos.append(temp_model.from_map(k1))

        return self

class DescribeDirQuotasResponseBodyDirQuotaInfosUserQuotaInfos(DaraModel):
    def __init__(
        self,
        file_count_limit: int = None,
        file_count_real: int = None,
        quota_type: str = None,
        size_limit: int = None,
        size_real: int = None,
        size_real_in_byte: int = None,
        user_id: str = None,
        user_type: str = None,
    ):
        # The maximum number of files that a user can create in the directory.
        self.file_count_limit = file_count_limit
        # The total number of files that a user has created in the directory.
        self.file_count_real = file_count_real
        # The type of the quota. Valid values: Accounting and Enforcement.
        self.quota_type = quota_type
        # The maximum size of files that a user can create in the directory. Unit: GiB.
        self.size_limit = size_limit
        # The total size of files that a user has created in the directory. Unit: GiB.
        self.size_real = size_real
        # The total size of files that a user has created in the directory. Unit: bytes.
        self.size_real_in_byte = size_real_in_byte
        # The ID of the user that you specify to create a quota for the directory. The value depends on the value of the UserType parameter. Valid values: Uid and Gid.
        self.user_id = user_id
        # The type of user. Valid values: Uid, Gid, and AllUsers.
        # 
        # *   If Uid or Gid is returned, a value is returned for UserId.
        # *   If AllUsers is returned, UserId is empty.
        self.user_type = user_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_count_limit is not None:
            result['FileCountLimit'] = self.file_count_limit

        if self.file_count_real is not None:
            result['FileCountReal'] = self.file_count_real

        if self.quota_type is not None:
            result['QuotaType'] = self.quota_type

        if self.size_limit is not None:
            result['SizeLimit'] = self.size_limit

        if self.size_real is not None:
            result['SizeReal'] = self.size_real

        if self.size_real_in_byte is not None:
            result['SizeRealInByte'] = self.size_real_in_byte

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_type is not None:
            result['UserType'] = self.user_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileCountLimit') is not None:
            self.file_count_limit = m.get('FileCountLimit')

        if m.get('FileCountReal') is not None:
            self.file_count_real = m.get('FileCountReal')

        if m.get('QuotaType') is not None:
            self.quota_type = m.get('QuotaType')

        if m.get('SizeLimit') is not None:
            self.size_limit = m.get('SizeLimit')

        if m.get('SizeReal') is not None:
            self.size_real = m.get('SizeReal')

        if m.get('SizeRealInByte') is not None:
            self.size_real_in_byte = m.get('SizeRealInByte')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')

        return self

