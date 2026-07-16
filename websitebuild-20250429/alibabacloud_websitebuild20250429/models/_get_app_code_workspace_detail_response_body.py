# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_websitebuild20250429 import models as main_models
from darabonba.model import DaraModel

class GetAppCodeWorkspaceDetailResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        allow_retry: bool = None,
        app_name: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_args: List[Any] = None,
        module: main_models.GetAppCodeWorkspaceDetailResponseBodyModule = None,
        request_id: str = None,
        root_error_code: str = None,
        root_error_msg: str = None,
        synchro: bool = None,
    ):
        # Detailed reason for access denial.
        self.access_denied_detail = access_denied_detail
        # Indicates whether retry is allowed. Valid values:  
        # - false: Retry is not allowed.  
        # - true: Retry is allowed.
        self.allow_retry = allow_retry
        # App name.
        self.app_name = app_name
        # Dynamic error code.
        self.dynamic_code = dynamic_code
        # Dynamic error message, used to replace the `%s` placeholder in the **ErrMessage** error message.  
        # > If **ErrMessage** returns **The Value of Input Parameter %s is not valid** and **DynamicMessage** returns **DtsJobId**, it indicates that the provided request parameter **DtsJobId** is invalid.
        self.dynamic_message = dynamic_message
        # Faulty parameters
        self.error_args = error_args
        # Application module
        self.module = module
        # Id of the request
        self.request_id = request_id
        # Error code
        self.root_error_code = root_error_code
        # Abnormal message
        self.root_error_msg = root_error_msg
        # Reserved parameter.
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
            temp_model = main_models.GetAppCodeWorkspaceDetailResponseBodyModule()
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

class GetAppCodeWorkspaceDetailResponseBodyModule(DaraModel):
    def __init__(
        self,
        active_logical_number: int = None,
        commit_hash: str = None,
        is_dirty: bool = None,
        max_logical_number: int = None,
        site_id: str = None,
        snapshots: List[main_models.GetAppCodeWorkspaceDetailResponseBodyModuleSnapshots] = None,
    ):
        # 11111
        self.active_logical_number = active_logical_number
        self.commit_hash = commit_hash
        # true
        self.is_dirty = is_dirty
        # 1111
        self.max_logical_number = max_logical_number
        # Site ID, which can be obtained by invoking the [ListSites](~~ListSites~~) API.
        self.site_id = site_id
        # API Guide information.
        self.snapshots = snapshots

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
        if self.active_logical_number is not None:
            result['ActiveLogicalNumber'] = self.active_logical_number

        if self.commit_hash is not None:
            result['CommitHash'] = self.commit_hash

        if self.is_dirty is not None:
            result['IsDirty'] = self.is_dirty

        if self.max_logical_number is not None:
            result['MaxLogicalNumber'] = self.max_logical_number

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        result['Snapshots'] = []
        if self.snapshots is not None:
            for k1 in self.snapshots:
                result['Snapshots'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveLogicalNumber') is not None:
            self.active_logical_number = m.get('ActiveLogicalNumber')

        if m.get('CommitHash') is not None:
            self.commit_hash = m.get('CommitHash')

        if m.get('IsDirty') is not None:
            self.is_dirty = m.get('IsDirty')

        if m.get('MaxLogicalNumber') is not None:
            self.max_logical_number = m.get('MaxLogicalNumber')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        self.snapshots = []
        if m.get('Snapshots') is not None:
            for k1 in m.get('Snapshots'):
                temp_model = main_models.GetAppCodeWorkspaceDetailResponseBodyModuleSnapshots()
                self.snapshots.append(temp_model.from_map(k1))

        return self

class GetAppCodeWorkspaceDetailResponseBodyModuleSnapshots(DaraModel):
    def __init__(
        self,
        change_log: str = None,
        gmt_create_time: str = None,
        logical_number: int = None,
    ):
        # SDK change log
        self.change_log = change_log
        # Creation UTC time in ISO8601 format.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ss.SSSZ
        self.gmt_create_time = gmt_create_time
        # Logical value
        self.logical_number = logical_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.change_log is not None:
            result['ChangeLog'] = self.change_log

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.logical_number is not None:
            result['LogicalNumber'] = self.logical_number

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeLog') is not None:
            self.change_log = m.get('ChangeLog')

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('LogicalNumber') is not None:
            self.logical_number = m.get('LogicalNumber')

        return self

