# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class ListDAGVersionsResponseBody(DaraModel):
    def __init__(
        self,
        dag_version_list: main_models.ListDAGVersionsResponseBodyDagVersionList = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The information about the published versions.
        self.dag_version_list = dag_version_list
        # The error code returned if the request fails.
        self.error_code = error_code
        # The error message returned if the request fails.
        self.error_message = error_message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values:
        # 
        # *   **true**: The request is successful.
        # *   **false**: The request fails.
        self.success = success
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.dag_version_list:
            self.dag_version_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dag_version_list is not None:
            result['DagVersionList'] = self.dag_version_list.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DagVersionList') is not None:
            temp_model = main_models.ListDAGVersionsResponseBodyDagVersionList()
            self.dag_version_list = temp_model.from_map(m.get('DagVersionList'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListDAGVersionsResponseBodyDagVersionList(DaraModel):
    def __init__(
        self,
        dag_version: List[main_models.ListDAGVersionsResponseBodyDagVersionListDagVersion] = None,
    ):
        self.dag_version = dag_version

    def validate(self):
        if self.dag_version:
            for v1 in self.dag_version:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DagVersion'] = []
        if self.dag_version is not None:
            for k1 in self.dag_version:
                result['DagVersion'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dag_version = []
        if m.get('DagVersion') is not None:
            for k1 in m.get('DagVersion'):
                temp_model = main_models.ListDAGVersionsResponseBodyDagVersionListDagVersion()
                self.dag_version.append(temp_model.from_map(k1))

        return self

class ListDAGVersionsResponseBodyDagVersionListDagVersion(DaraModel):
    def __init__(
        self,
        dag_name: str = None,
        dag_owner_id: str = None,
        dag_owner_nick_name: str = None,
        last_version_id: int = None,
        version_comments: str = None,
        version_id: int = None,
    ):
        # The name of the task flow.
        self.dag_name = dag_name
        # The ID of the task flow owner.
        self.dag_owner_id = dag_owner_id
        # The name of the task flow owner.
        self.dag_owner_nick_name = dag_owner_nick_name
        # The ID of the previously published version.
        self.last_version_id = last_version_id
        # The description of the version.
        self.version_comments = version_comments
        # The ID of the version.
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dag_name is not None:
            result['DagName'] = self.dag_name

        if self.dag_owner_id is not None:
            result['DagOwnerId'] = self.dag_owner_id

        if self.dag_owner_nick_name is not None:
            result['DagOwnerNickName'] = self.dag_owner_nick_name

        if self.last_version_id is not None:
            result['LastVersionId'] = self.last_version_id

        if self.version_comments is not None:
            result['VersionComments'] = self.version_comments

        if self.version_id is not None:
            result['VersionId'] = self.version_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DagName') is not None:
            self.dag_name = m.get('DagName')

        if m.get('DagOwnerId') is not None:
            self.dag_owner_id = m.get('DagOwnerId')

        if m.get('DagOwnerNickName') is not None:
            self.dag_owner_nick_name = m.get('DagOwnerNickName')

        if m.get('LastVersionId') is not None:
            self.last_version_id = m.get('LastVersionId')

        if m.get('VersionComments') is not None:
            self.version_comments = m.get('VersionComments')

        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')

        return self

