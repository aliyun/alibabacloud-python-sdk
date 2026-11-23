# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_marketing_event20210101 import models as main_models
from darabonba.model import DaraModel

class MosQueryRegistrationInfoResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: main_models.MosQueryRegistrationInfoResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.MosQueryRegistrationInfoResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class MosQueryRegistrationInfoResponseBodyData(DaraModel):
    def __init__(
        self,
        list: List[main_models.MosQueryRegistrationInfoResponseBodyDataList] = None,
        total: int = None,
    ):
        self.list = list
        self.total = total

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['List'] = []
        if self.list is not None:
            for k1 in self.list:
                result['List'].append(k1.to_map() if k1 else None)

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.MosQueryRegistrationInfoResponseBodyDataList()
                self.list.append(temp_model.from_map(k1))

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class MosQueryRegistrationInfoResponseBodyDataList(DaraModel):
    def __init__(
        self,
        activity_id: str = None,
        channel_name: str = None,
        checkin_status: str = None,
        id: int = None,
        qr_code: str = None,
        tag_infos: List[main_models.MosQueryRegistrationInfoResponseBodyDataListTagInfos] = None,
        user_company: str = None,
        user_email: str = None,
        user_name: str = None,
        user_phone: str = None,
    ):
        self.activity_id = activity_id
        self.channel_name = channel_name
        self.checkin_status = checkin_status
        self.id = id
        self.qr_code = qr_code
        self.tag_infos = tag_infos
        self.user_company = user_company
        self.user_email = user_email
        self.user_name = user_name
        self.user_phone = user_phone

    def validate(self):
        if self.tag_infos:
            for v1 in self.tag_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.activity_id is not None:
            result['ActivityId'] = self.activity_id

        if self.channel_name is not None:
            result['ChannelName'] = self.channel_name

        if self.checkin_status is not None:
            result['CheckinStatus'] = self.checkin_status

        if self.id is not None:
            result['Id'] = self.id

        if self.qr_code is not None:
            result['QrCode'] = self.qr_code

        result['TagInfos'] = []
        if self.tag_infos is not None:
            for k1 in self.tag_infos:
                result['TagInfos'].append(k1.to_map() if k1 else None)

        if self.user_company is not None:
            result['UserCompany'] = self.user_company

        if self.user_email is not None:
            result['UserEmail'] = self.user_email

        if self.user_name is not None:
            result['UserName'] = self.user_name

        if self.user_phone is not None:
            result['UserPhone'] = self.user_phone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivityId') is not None:
            self.activity_id = m.get('ActivityId')

        if m.get('ChannelName') is not None:
            self.channel_name = m.get('ChannelName')

        if m.get('CheckinStatus') is not None:
            self.checkin_status = m.get('CheckinStatus')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('QrCode') is not None:
            self.qr_code = m.get('QrCode')

        self.tag_infos = []
        if m.get('TagInfos') is not None:
            for k1 in m.get('TagInfos'):
                temp_model = main_models.MosQueryRegistrationInfoResponseBodyDataListTagInfos()
                self.tag_infos.append(temp_model.from_map(k1))

        if m.get('UserCompany') is not None:
            self.user_company = m.get('UserCompany')

        if m.get('UserEmail') is not None:
            self.user_email = m.get('UserEmail')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        if m.get('UserPhone') is not None:
            self.user_phone = m.get('UserPhone')

        return self

class MosQueryRegistrationInfoResponseBodyDataListTagInfos(DaraModel):
    def __init__(
        self,
        tag_code: str = None,
        tag_name: str = None,
    ):
        self.tag_code = tag_code
        self.tag_name = tag_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_code is not None:
            result['TagCode'] = self.tag_code

        if self.tag_name is not None:
            result['TagName'] = self.tag_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagCode') is not None:
            self.tag_code = m.get('TagCode')

        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')

        return self

