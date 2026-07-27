# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_websitebuild20250429 import models as main_models
from darabonba.model import DaraModel

class ListAppPluginVersionsResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        allow_retry: bool = None,
        app_name: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_args: List[Any] = None,
        module: main_models.ListAppPluginVersionsResponseBodyModule = None,
        request_id: str = None,
        root_error_code: str = None,
        root_error_msg: str = None,
        synchro: bool = None,
    ):
        # The detailed reason why access was denied.
        self.access_denied_detail = access_denied_detail
        # Indicates whether retry is allowed.
        self.allow_retry = allow_retry
        # The application name. The application with this name is queried.
        self.app_name = app_name
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic message. Currently not in use. Ignore this parameter.
        self.dynamic_message = dynamic_message
        # The error parameters returned.
        self.error_args = error_args
        # The response data.
        self.module = module
        # Id of the request
        self.request_id = request_id
        # The error code.
        self.root_error_code = root_error_code
        # The exception message.
        self.root_error_msg = root_error_msg
        # The reserved parameter.
        self.synchro = synchro

    def validate(self):
        if self.module:
            self.module.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.allow_retry is not None:
            result['AllowRetry'] = self.allow_retry

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code

        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message

        if self.error_args is not None:
            result['ErrorArgs'] = self.error_args

        if self.module is not None:
            result['Module'] = self.module.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.root_error_code is not None:
            result['RootErrorCode'] = self.root_error_code

        if self.root_error_msg is not None:
            result['RootErrorMsg'] = self.root_error_msg

        if self.synchro is not None:
            result['Synchro'] = self.synchro

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('AllowRetry') is not None:
            self.allow_retry = m.get('AllowRetry')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')

        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')

        if m.get('ErrorArgs') is not None:
            self.error_args = m.get('ErrorArgs')

        if m.get('Module') is not None:
            temp_model = main_models.ListAppPluginVersionsResponseBodyModule()
            self.module = temp_model.from_map(m.get('Module'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RootErrorCode') is not None:
            self.root_error_code = m.get('RootErrorCode')

        if m.get('RootErrorMsg') is not None:
            self.root_error_msg = m.get('RootErrorMsg')

        if m.get('Synchro') is not None:
            self.synchro = m.get('Synchro')

        return self

class ListAppPluginVersionsResponseBodyModule(DaraModel):
    def __init__(
        self,
        current_page_num: int = None,
        data: List[main_models.ListAppPluginVersionsResponseBodyModuleData] = None,
        next: main_models.ListAppPluginVersionsResponseBodyModuleNext = None,
        next_page: bool = None,
        page_size: int = None,
        pre_page: bool = None,
        result_limit: bool = None,
        total_item_num: int = None,
        total_page_num: int = None,
    ):
        # The current page number.
        self.current_page_num = current_page_num
        # The query results.
        self.data = data
        # The decision weight.
        self.next = next
        # Indicates whether a next page exists.
        self.next_page = next_page
        # The number of entries per page.
        self.page_size = page_size
        # Indicates whether a previous page exists.
        self.pre_page = pre_page
        # Apart from pagination limits, the server processes a maximum of 1000 recent records for the current query. If the results exceed 1000 records, **ResultLimit** is **true**, and you need to narrow the time range and search again. Otherwise, **ResultLimit** is **false**.
        self.result_limit = result_limit
        # The total number of entries.
        self.total_item_num = total_item_num
        # The total number of pages.
        self.total_page_num = total_page_num

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()
        if self.next:
            self.next.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.next is not None:
            result['Next'] = self.next.to_map()

        if self.next_page is not None:
            result['NextPage'] = self.next_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.pre_page is not None:
            result['PrePage'] = self.pre_page

        if self.result_limit is not None:
            result['ResultLimit'] = self.result_limit

        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num

        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListAppPluginVersionsResponseBodyModuleData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Next') is not None:
            temp_model = main_models.ListAppPluginVersionsResponseBodyModuleNext()
            self.next = temp_model.from_map(m.get('Next'))

        if m.get('NextPage') is not None:
            self.next_page = m.get('NextPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PrePage') is not None:
            self.pre_page = m.get('PrePage')

        if m.get('ResultLimit') is not None:
            self.result_limit = m.get('ResultLimit')

        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')

        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')

        return self

class ListAppPluginVersionsResponseBodyModuleNext(DaraModel):
    def __init__(
        self,
        changelog: str = None,
        commit_sha: str = None,
        created_by: str = None,
        file_count: int = None,
        gmt_create: str = None,
        status: str = None,
        version: str = None,
    ):
        # The version changelog.
        self.changelog = changelog
        # The commit ID.
        self.commit_sha = commit_sha
        # The creator.
        self.created_by = created_by
        # The current number of files in the project.
        self.file_count = file_count
        # The creation time.
        self.gmt_create = gmt_create
        # Valid values: unknown, init, testing, online.
        self.status = status
        # The application instance version.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.changelog is not None:
            result['Changelog'] = self.changelog

        if self.commit_sha is not None:
            result['CommitSha'] = self.commit_sha

        if self.created_by is not None:
            result['CreatedBy'] = self.created_by

        if self.file_count is not None:
            result['FileCount'] = self.file_count

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.status is not None:
            result['Status'] = self.status

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Changelog') is not None:
            self.changelog = m.get('Changelog')

        if m.get('CommitSha') is not None:
            self.commit_sha = m.get('CommitSha')

        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')

        if m.get('FileCount') is not None:
            self.file_count = m.get('FileCount')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class ListAppPluginVersionsResponseBodyModuleData(DaraModel):
    def __init__(
        self,
        changelog: str = None,
        commit_sha: str = None,
        created_by: str = None,
        file_count: int = None,
        gmt_create: str = None,
        status: str = None,
        version: str = None,
    ):
        # The version changelog.
        self.changelog = changelog
        # The commit ID.
        self.commit_sha = commit_sha
        # The creator.
        self.created_by = created_by
        # The current number of files in the project.
        self.file_count = file_count
        # The creation time.
        self.gmt_create = gmt_create
        # The file status.
        self.status = status
        # The application instance version.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.changelog is not None:
            result['Changelog'] = self.changelog

        if self.commit_sha is not None:
            result['CommitSha'] = self.commit_sha

        if self.created_by is not None:
            result['CreatedBy'] = self.created_by

        if self.file_count is not None:
            result['FileCount'] = self.file_count

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.status is not None:
            result['Status'] = self.status

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Changelog') is not None:
            self.changelog = m.get('Changelog')

        if m.get('CommitSha') is not None:
            self.commit_sha = m.get('CommitSha')

        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')

        if m.get('FileCount') is not None:
            self.file_count = m.get('FileCount')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

