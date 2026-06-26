# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_websitebuild20250429 import models as main_models
from darabonba.model import DaraModel

class ListPromotionOfferRecordsForPartnerResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        allow_retry: bool = None,
        app_name: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_args: List[Any] = None,
        max_results: int = None,
        module: main_models.ListPromotionOfferRecordsForPartnerResponseBodyModule = None,
        next_token: str = None,
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
        # The dynamic error message, which is used to replace the %s variable in the ErrMessage response parameter.
        self.dynamic_message = dynamic_message
        # The error parameters.
        self.error_args = error_args
        # The number of entries per query.
        # 
        # Valid values: 10 to 100. Default value: 20.
        self.max_results = max_results
        # The response data.
        self.module = module
        # The token for the next query. This parameter is empty if no more results exist.
        self.next_token = next_token
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

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.module is not None:
            result['Module'] = self.module.to_map()

        if self.next_token is not None:
            result['NextToken'] = self.next_token

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

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('Module') is not None:
            temp_model = main_models.ListPromotionOfferRecordsForPartnerResponseBodyModule()
            self.module = temp_model.from_map(m.get('Module'))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RootErrorCode') is not None:
            self.root_error_code = m.get('RootErrorCode')

        if m.get('RootErrorMsg') is not None:
            self.root_error_msg = m.get('RootErrorMsg')

        if m.get('Synchro') is not None:
            self.synchro = m.get('Synchro')

        return self

class ListPromotionOfferRecordsForPartnerResponseBodyModule(DaraModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        records: List[main_models.ListPromotionOfferRecordsForPartnerResponseBodyModuleRecords] = None,
        total_count: int = None,
    ):
        # The page number.
        self.page_num = page_num
        # The number of entries per page.
        self.page_size = page_size
        # The list of issuance records.
        self.records = records
        # The total number of records.
        self.total_count = total_count

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
        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['Records'] = []
        if self.records is not None:
            for k1 in self.records:
                result['Records'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.records = []
        if m.get('Records') is not None:
            for k1 in m.get('Records'):
                temp_model = main_models.ListPromotionOfferRecordsForPartnerResponseBodyModuleRecords()
                self.records.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListPromotionOfferRecordsForPartnerResponseBodyModuleRecords(DaraModel):
    def __init__(
        self,
        activity_code: str = None,
        activity_name: str = None,
        employee_code: str = None,
        fail_reason: str = None,
        issuance_time: str = None,
        offer_snapshot: str = None,
        record_id: str = None,
        remark: str = None,
        status: str = None,
        user_id: str = None,
    ):
        # The activity code.
        self.activity_code = activity_code
        # The activity name.
        self.activity_name = activity_name
        # The employee code.
        self.employee_code = employee_code
        # The failure reason.
        self.fail_reason = fail_reason
        # The issuance time.
        self.issuance_time = issuance_time
        # The benefit snapshot in JSON format.
        self.offer_snapshot = offer_snapshot
        # The record ID.
        self.record_id = record_id
        # The operation remark.
        self.remark = remark
        # The issuance status.
        self.status = status
        # The user ID.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.activity_code is not None:
            result['ActivityCode'] = self.activity_code

        if self.activity_name is not None:
            result['ActivityName'] = self.activity_name

        if self.employee_code is not None:
            result['EmployeeCode'] = self.employee_code

        if self.fail_reason is not None:
            result['FailReason'] = self.fail_reason

        if self.issuance_time is not None:
            result['IssuanceTime'] = self.issuance_time

        if self.offer_snapshot is not None:
            result['OfferSnapshot'] = self.offer_snapshot

        if self.record_id is not None:
            result['RecordId'] = self.record_id

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.status is not None:
            result['Status'] = self.status

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivityCode') is not None:
            self.activity_code = m.get('ActivityCode')

        if m.get('ActivityName') is not None:
            self.activity_name = m.get('ActivityName')

        if m.get('EmployeeCode') is not None:
            self.employee_code = m.get('EmployeeCode')

        if m.get('FailReason') is not None:
            self.fail_reason = m.get('FailReason')

        if m.get('IssuanceTime') is not None:
            self.issuance_time = m.get('IssuanceTime')

        if m.get('OfferSnapshot') is not None:
            self.offer_snapshot = m.get('OfferSnapshot')

        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

