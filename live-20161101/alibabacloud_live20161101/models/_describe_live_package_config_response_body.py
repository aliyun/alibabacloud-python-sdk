# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeLivePackageConfigResponseBody(DaraModel):
    def __init__(
        self,
        live_package_config_list: main_models.DescribeLivePackageConfigResponseBodyLivePackageConfigList = None,
        order: str = None,
        page_num: int = None,
        page_size: int = None,
        request_id: str = None,
        total_num: int = None,
        total_page: int = None,
    ):
        # The live stream encapsulation configurations.
        self.live_package_config_list = live_package_config_list
        # The sorting order. Valid values:
        # 
        # *   **asc** (default): ascending order
        # *   **desc**: descending order
        self.order = order
        # The page number.
        self.page_num = page_num
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of live stream encapsulation configurations.
        self.total_num = total_num
        # The total number of pages.
        self.total_page = total_page

    def validate(self):
        if self.live_package_config_list:
            self.live_package_config_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.live_package_config_list is not None:
            result['LivePackageConfigList'] = self.live_package_config_list.to_map()

        if self.order is not None:
            result['Order'] = self.order

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_num is not None:
            result['TotalNum'] = self.total_num

        if self.total_page is not None:
            result['TotalPage'] = self.total_page

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LivePackageConfigList') is not None:
            temp_model = main_models.DescribeLivePackageConfigResponseBodyLivePackageConfigList()
            self.live_package_config_list = temp_model.from_map(m.get('LivePackageConfigList'))

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')

        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')

        return self

class DescribeLivePackageConfigResponseBodyLivePackageConfigList(DaraModel):
    def __init__(
        self,
        live_package_config: List[main_models.DescribeLivePackageConfigResponseBodyLivePackageConfigListLivePackageConfig] = None,
    ):
        self.live_package_config = live_package_config

    def validate(self):
        if self.live_package_config:
            for v1 in self.live_package_config:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LivePackageConfig'] = []
        if self.live_package_config is not None:
            for k1 in self.live_package_config:
                result['LivePackageConfig'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.live_package_config = []
        if m.get('LivePackageConfig') is not None:
            for k1 in m.get('LivePackageConfig'):
                temp_model = main_models.DescribeLivePackageConfigResponseBodyLivePackageConfigListLivePackageConfig()
                self.live_package_config.append(temp_model.from_map(k1))

        return self

class DescribeLivePackageConfigResponseBodyLivePackageConfigListLivePackageConfig(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        domain_name: str = None,
        ignore_transcode: bool = None,
        part_duration: int = None,
        protocol: str = None,
        segment_duration: int = None,
        segment_num: int = None,
        stream_name: str = None,
    ):
        # The application name.
        self.app_name = app_name
        # The main streaming domain.
        self.domain_name = domain_name
        # Indicates whether the transcoded stream is ignored. Valid values:
        # 
        # *   **true** (default)
        # *   **false**
        self.ignore_transcode = ignore_transcode
        # The part length. Unit: milliseconds.
        self.part_duration = part_duration
        # The streaming protocol and encapsulation format.
        self.protocol = protocol
        # The segment length. Unit: seconds.
        self.segment_duration = segment_duration
        # The number of segments.
        self.segment_num = segment_num
        # The stream name.
        self.stream_name = stream_name

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

        if self.ignore_transcode is not None:
            result['IgnoreTranscode'] = self.ignore_transcode

        if self.part_duration is not None:
            result['PartDuration'] = self.part_duration

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.segment_duration is not None:
            result['SegmentDuration'] = self.segment_duration

        if self.segment_num is not None:
            result['SegmentNum'] = self.segment_num

        if self.stream_name is not None:
            result['StreamName'] = self.stream_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('IgnoreTranscode') is not None:
            self.ignore_transcode = m.get('IgnoreTranscode')

        if m.get('PartDuration') is not None:
            self.part_duration = m.get('PartDuration')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('SegmentDuration') is not None:
            self.segment_duration = m.get('SegmentDuration')

        if m.get('SegmentNum') is not None:
            self.segment_num = m.get('SegmentNum')

        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')

        return self

