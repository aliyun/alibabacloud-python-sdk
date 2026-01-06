# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetUserLatestPlanResponseBody(DaraModel):
    def __init__(
        self,
        account_handle_status: int = None,
        account_handle_time: str = None,
        account_type: int = None,
        agreement_first_sign_time: str = None,
        agreement_last_sign_time: str = None,
        agreement_status: int = None,
        data_handle_end_time: str = None,
        data_handle_start_time: str = None,
        data_handle_status: int = None,
        exclusive_plan: int = None,
        new_account_uid: int = None,
        request_id: str = None,
        status: int = None,
        vendor_request_id: str = None,
        vendor_type: str = None,
    ):
        self.account_handle_status = account_handle_status
        self.account_handle_time = account_handle_time
        self.account_type = account_type
        self.agreement_first_sign_time = agreement_first_sign_time
        self.agreement_last_sign_time = agreement_last_sign_time
        self.agreement_status = agreement_status
        self.data_handle_end_time = data_handle_end_time
        self.data_handle_start_time = data_handle_start_time
        self.data_handle_status = data_handle_status
        self.exclusive_plan = exclusive_plan
        self.new_account_uid = new_account_uid
        self.request_id = request_id
        self.status = status
        self.vendor_request_id = vendor_request_id
        self.vendor_type = vendor_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_handle_status is not None:
            result['accountHandleStatus'] = self.account_handle_status

        if self.account_handle_time is not None:
            result['accountHandleTime'] = self.account_handle_time

        if self.account_type is not None:
            result['accountType'] = self.account_type

        if self.agreement_first_sign_time is not None:
            result['agreementFirstSignTime'] = self.agreement_first_sign_time

        if self.agreement_last_sign_time is not None:
            result['agreementLastSignTime'] = self.agreement_last_sign_time

        if self.agreement_status is not None:
            result['agreementStatus'] = self.agreement_status

        if self.data_handle_end_time is not None:
            result['dataHandleEndTime'] = self.data_handle_end_time

        if self.data_handle_start_time is not None:
            result['dataHandleStartTime'] = self.data_handle_start_time

        if self.data_handle_status is not None:
            result['dataHandleStatus'] = self.data_handle_status

        if self.exclusive_plan is not None:
            result['exclusivePlan'] = self.exclusive_plan

        if self.new_account_uid is not None:
            result['newAccountUid'] = self.new_account_uid

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.status is not None:
            result['status'] = self.status

        if self.vendor_request_id is not None:
            result['vendorRequestId'] = self.vendor_request_id

        if self.vendor_type is not None:
            result['vendorType'] = self.vendor_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountHandleStatus') is not None:
            self.account_handle_status = m.get('accountHandleStatus')

        if m.get('accountHandleTime') is not None:
            self.account_handle_time = m.get('accountHandleTime')

        if m.get('accountType') is not None:
            self.account_type = m.get('accountType')

        if m.get('agreementFirstSignTime') is not None:
            self.agreement_first_sign_time = m.get('agreementFirstSignTime')

        if m.get('agreementLastSignTime') is not None:
            self.agreement_last_sign_time = m.get('agreementLastSignTime')

        if m.get('agreementStatus') is not None:
            self.agreement_status = m.get('agreementStatus')

        if m.get('dataHandleEndTime') is not None:
            self.data_handle_end_time = m.get('dataHandleEndTime')

        if m.get('dataHandleStartTime') is not None:
            self.data_handle_start_time = m.get('dataHandleStartTime')

        if m.get('dataHandleStatus') is not None:
            self.data_handle_status = m.get('dataHandleStatus')

        if m.get('exclusivePlan') is not None:
            self.exclusive_plan = m.get('exclusivePlan')

        if m.get('newAccountUid') is not None:
            self.new_account_uid = m.get('newAccountUid')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('vendorRequestId') is not None:
            self.vendor_request_id = m.get('vendorRequestId')

        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')

        return self

