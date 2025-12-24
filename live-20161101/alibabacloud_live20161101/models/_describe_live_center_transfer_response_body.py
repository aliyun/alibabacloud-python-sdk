# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeLiveCenterTransferResponseBody(DaraModel):
    def __init__(
        self,
        live_center_transfer_info_list: main_models.DescribeLiveCenterTransferResponseBodyLiveCenterTransferInfoList = None,
        request_id: str = None,
    ):
        # The stream relay information.
        self.live_center_transfer_info_list = live_center_transfer_info_list
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.live_center_transfer_info_list:
            self.live_center_transfer_info_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.live_center_transfer_info_list is not None:
            result['LiveCenterTransferInfoList'] = self.live_center_transfer_info_list.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LiveCenterTransferInfoList') is not None:
            temp_model = main_models.DescribeLiveCenterTransferResponseBodyLiveCenterTransferInfoList()
            self.live_center_transfer_info_list = temp_model.from_map(m.get('LiveCenterTransferInfoList'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeLiveCenterTransferResponseBodyLiveCenterTransferInfoList(DaraModel):
    def __init__(
        self,
        live_center_transfer_info: List[main_models.DescribeLiveCenterTransferResponseBodyLiveCenterTransferInfoListLiveCenterTransferInfo] = None,
    ):
        self.live_center_transfer_info = live_center_transfer_info

    def validate(self):
        if self.live_center_transfer_info:
            for v1 in self.live_center_transfer_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LiveCenterTransferInfo'] = []
        if self.live_center_transfer_info is not None:
            for k1 in self.live_center_transfer_info:
                result['LiveCenterTransferInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.live_center_transfer_info = []
        if m.get('LiveCenterTransferInfo') is not None:
            for k1 in m.get('LiveCenterTransferInfo'):
                temp_model = main_models.DescribeLiveCenterTransferResponseBodyLiveCenterTransferInfoListLiveCenterTransferInfo()
                self.live_center_transfer_info.append(temp_model.from_map(k1))

        return self

class DescribeLiveCenterTransferResponseBodyLiveCenterTransferInfoListLiveCenterTransferInfo(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        domain_name: str = None,
        dst_url: str = None,
        end_time: str = None,
        start_time: str = None,
        stream_name: str = None,
        transfer_args: str = None,
    ):
        # The name of the application to which the live stream belongs.
        self.app_name = app_name
        # The streaming domain.
        self.domain_name = domain_name
        # The third-party URL to which the live stream is relayed.
        self.dst_url = dst_url
        # The end time of stream relay.
        self.end_time = end_time
        # The start time of stream relay.
        self.start_time = start_time
        # The name of the live stream.
        self.stream_name = stream_name
        # The validity period of stream relay. Valid values:
        # 
        # *   **always**: The stream can always be relayed.
        # *   **time**: The stream can be relayed in a specified time period.
        self.transfer_args = transfer_args

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.dst_url is not None:
            result['DstUrl'] = self.dst_url

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.stream_name is not None:
            result['StreamName'] = self.stream_name

        if self.transfer_args is not None:
            result['TransferArgs'] = self.transfer_args

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('DstUrl') is not None:
            self.dst_url = m.get('DstUrl')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')

        if m.get('TransferArgs') is not None:
            self.transfer_args = m.get('TransferArgs')

        return self

