# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateLiveCenterTransferRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        domain_name: str = None,
        dst_url: str = None,
        end_time: str = None,
        owner_id: int = None,
        region_id: str = None,
        start_time: str = None,
        stream_name: str = None,
        transfer_args: str = None,
    ):
        # The name of the live stream application. The AppName you enter must match the AppName of the live stream to be transferred for the configuration to take effect. You can view the AppName on the [Stream Management](https://help.aliyun.com/document_detail/197397.html) page.
        # 
        # This parameter is required.
        self.app_name = app_name
        # The streaming domain.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # The third-party live streaming address to transfer to. A maximum of one address is supported.
        # 
        # >The protocol of the destination address must match the protocol of the live stream being transferred. Only RTMP and SRT protocols are supported.
        # 
        # This parameter is required.
        self.dst_url = dst_url
        # The end time of the transfer. The date format follows ISO 8601 and uses UTC+0 time in the format yyyy-MM-ddTHH:mm:ssZ.
        # 
        # >The end time must be later than the start time.
        self.end_time = end_time
        self.owner_id = owner_id
        # The region ID.
        self.region_id = region_id
        # The start time of the transfer. The date format follows ISO 8601 and uses UTC+0 time in the format yyyy-MM-ddTHH:mm:ssZ.
        self.start_time = start_time
        # The name of the live stream. You can view the StreamName on the [Stream Management](https://help.aliyun.com/document_detail/197397.html) page.
        # 
        # This parameter is required.
        self.stream_name = stream_name
        # The transfer validity period. Valid values:
        # 
        # - **always**: Permanently effective.
        # 
        # - **time**: Effective within a specified time range.
        # 
        # >If you set this parameter to **time**, **StartTime** and **EndTime** are required.
        # 
        # This parameter is required.
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

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

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

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')

        if m.get('TransferArgs') is not None:
            self.transfer_args = m.get('TransferArgs')

        return self

