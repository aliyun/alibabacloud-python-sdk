# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class GetDingtalkProjectionListResponseBody(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        data: List[main_models.GetDingtalkProjectionListResponseBodyData] = None,
        request_id: str = None,
        total_count: int = None,
        vendor_request_id: str = None,
        vendor_type: str = None,
    ):
        self.current_page = current_page
        self.data = data
        self.request_id = request_id
        self.total_count = total_count
        self.vendor_request_id = vendor_request_id
        self.vendor_type = vendor_type

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['currentPage'] = self.current_page

        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        if self.vendor_request_id is not None:
            result['vendorRequestId'] = self.vendor_request_id

        if self.vendor_type is not None:
            result['vendorType'] = self.vendor_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')

        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.GetDingtalkProjectionListResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        if m.get('vendorRequestId') is not None:
            self.vendor_request_id = m.get('vendorRequestId')

        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')

        return self

class GetDingtalkProjectionListResponseBodyData(DaraModel):
    def __init__(
        self,
        call_status: str = None,
        code: str = None,
        dev_uid: int = None,
        duration: str = None,
        end_ts: int = None,
        nick_code: str = None,
        org_id: int = None,
        recv_client_id: str = None,
        recv_client_name: str = None,
        send_client_id: str = None,
        send_client_name: str = None,
        send_client_work_no: str = None,
        start_ts: int = None,
        time_str: str = None,
    ):
        self.call_status = call_status
        self.code = code
        self.dev_uid = dev_uid
        self.duration = duration
        self.end_ts = end_ts
        self.nick_code = nick_code
        self.org_id = org_id
        self.recv_client_id = recv_client_id
        self.recv_client_name = recv_client_name
        self.send_client_id = send_client_id
        self.send_client_name = send_client_name
        self.send_client_work_no = send_client_work_no
        self.start_ts = start_ts
        self.time_str = time_str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.call_status is not None:
            result['callStatus'] = self.call_status

        if self.code is not None:
            result['code'] = self.code

        if self.dev_uid is not None:
            result['devUid'] = self.dev_uid

        if self.duration is not None:
            result['duration'] = self.duration

        if self.end_ts is not None:
            result['endTs'] = self.end_ts

        if self.nick_code is not None:
            result['nickCode'] = self.nick_code

        if self.org_id is not None:
            result['orgId'] = self.org_id

        if self.recv_client_id is not None:
            result['recvClientId'] = self.recv_client_id

        if self.recv_client_name is not None:
            result['recvClientName'] = self.recv_client_name

        if self.send_client_id is not None:
            result['sendClientId'] = self.send_client_id

        if self.send_client_name is not None:
            result['sendClientName'] = self.send_client_name

        if self.send_client_work_no is not None:
            result['sendClientWorkNo'] = self.send_client_work_no

        if self.start_ts is not None:
            result['startTs'] = self.start_ts

        if self.time_str is not None:
            result['timeStr'] = self.time_str

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('callStatus') is not None:
            self.call_status = m.get('callStatus')

        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('devUid') is not None:
            self.dev_uid = m.get('devUid')

        if m.get('duration') is not None:
            self.duration = m.get('duration')

        if m.get('endTs') is not None:
            self.end_ts = m.get('endTs')

        if m.get('nickCode') is not None:
            self.nick_code = m.get('nickCode')

        if m.get('orgId') is not None:
            self.org_id = m.get('orgId')

        if m.get('recvClientId') is not None:
            self.recv_client_id = m.get('recvClientId')

        if m.get('recvClientName') is not None:
            self.recv_client_name = m.get('recvClientName')

        if m.get('sendClientId') is not None:
            self.send_client_id = m.get('sendClientId')

        if m.get('sendClientName') is not None:
            self.send_client_name = m.get('sendClientName')

        if m.get('sendClientWorkNo') is not None:
            self.send_client_work_no = m.get('sendClientWorkNo')

        if m.get('startTs') is not None:
            self.start_ts = m.get('startTs')

        if m.get('timeStr') is not None:
            self.time_str = m.get('timeStr')

        return self

