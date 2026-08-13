# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_websitebuild20250429 import models as main_models
from darabonba.model import DaraModel

class BindAppDomainResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        allow_retry: bool = None,
        app_name: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_args: List[Any] = None,
        module: main_models.BindAppDomainResponseBodyModule = None,
        request_id: str = None,
        root_error_code: str = None,
        root_error_msg: str = None,
        synchro: bool = None,
    ):
        # The detailed reason why access is denied.
        self.access_denied_detail = access_denied_detail
        # Indicates whether retry is allowed.
        self.allow_retry = allow_retry
        # The application name.
        self.app_name = app_name
        # The error code.
        self.dynamic_code = dynamic_code
        # The dynamic error message used to replace the **%s** variable in the **ErrMessage** parameter.
        # > For example, if **ErrMessage** returns **The Value of Input Parameter %s is not valid** and **DynamicMessage** returns **DtsJobId**, the request parameter **DtsJobId** is invalid.
        self.dynamic_message = dynamic_message
        # The error parameters.
        self.error_args = error_args
        # The data table module. Valid values:
        # 
        # - ABTest: experiment data table.
        # 
        # - ExperimentTool: experiment tool table.
        # 
        # - DataDiagnosis: data diagnostics.
        self.module = module
        # Id of the request
        self.request_id = request_id
        # The root error code.
        self.root_error_code = root_error_code
        # The root error message.
        self.root_error_msg = root_error_msg
        # Indicates whether the request is processed synchronously.
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
            temp_model = main_models.BindAppDomainResponseBodyModule()
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

class BindAppDomainResponseBodyModule(DaraModel):
    def __init__(
        self,
        dns_conflict: main_models.BindAppDomainResponseBodyModuleDnsConflict = None,
        success: bool = None,
    ):
        # The DNS conflict information. This parameter is returned when a conflict is detected during synchronous verification.
        self.dns_conflict = dns_conflict
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        if self.dns_conflict:
            self.dns_conflict.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dns_conflict is not None:
            result['DnsConflict'] = self.dns_conflict.to_map()

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DnsConflict') is not None:
            temp_model = main_models.BindAppDomainResponseBodyModuleDnsConflict()
            self.dns_conflict = temp_model.from_map(m.get('DnsConflict'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class BindAppDomainResponseBodyModuleDnsConflict(DaraModel):
    def __init__(
        self,
        can_auto_resolve: bool = None,
        has_conflict: bool = None,
        message: str = None,
        records: List[main_models.BindAppDomainResponseBodyModuleDnsConflictRecords] = None,
    ):
        # Indicates whether automatic override is supported. The value is true for the current Alibaba Cloud account and false for other accounts.
        self.can_auto_resolve = can_auto_resolve
        # Indicates whether a conflict exists.
        self.has_conflict = has_conflict
        # The user-facing prompt message. Different guidance messages are generated based on the scenario.
        self.message = message
        # The list of conflicting DNS records (reusing the existing AppDomainDnsRecordDTO).
        self.records = records

    def validate(self):
        if self.records:
            for v1 in self.records:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.can_auto_resolve is not None:
            result['CanAutoResolve'] = self.can_auto_resolve

        if self.has_conflict is not None:
            result['HasConflict'] = self.has_conflict

        if self.message is not None:
            result['Message'] = self.message

        result['Records'] = []
        if self.records is not None:
            for k1 in self.records:
                result['Records'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanAutoResolve') is not None:
            self.can_auto_resolve = m.get('CanAutoResolve')

        if m.get('HasConflict') is not None:
            self.has_conflict = m.get('HasConflict')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        self.records = []
        if m.get('Records') is not None:
            for k1 in m.get('Records'):
                temp_model = main_models.BindAppDomainResponseBodyModuleDnsConflictRecords()
                self.records.append(temp_model.from_map(k1))

        return self

class BindAppDomainResponseBodyModuleDnsConflictRecords(DaraModel):
    def __init__(
        self,
        host: str = None,
        record_type: str = None,
        status: str = None,
        value: str = None,
    ):
        # The host record.
        self.host = host
        # The record type.
        self.record_type = record_type
        self.status = status
        # The record value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.host is not None:
            result['Host'] = self.host

        if self.record_type is not None:
            result['RecordType'] = self.record_type

        if self.status is not None:
            result['Status'] = self.status

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Host') is not None:
            self.host = m.get('Host')

        if m.get('RecordType') is not None:
            self.record_type = m.get('RecordType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

