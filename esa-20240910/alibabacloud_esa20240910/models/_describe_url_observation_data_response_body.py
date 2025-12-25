# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class DescribeUrlObservationDataResponseBody(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        request_id: str = None,
        start_time: str = None,
        url_detail_data: List[main_models.DescribeUrlObservationDataResponseBodyUrlDetailData] = None,
    ):
        # The end of the time range during which data was queried.
        # 
        # Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC. The time must be in UTC.
        self.end_time = end_time
        # The request ID.
        self.request_id = request_id
        # The create time. The time is in the yyyy-MM-ddTHH:mm:ssZ format.
        self.start_time = start_time
        # The objects that are returned.
        self.url_detail_data = url_detail_data

    def validate(self):
        if self.url_detail_data:
            for v1 in self.url_detail_data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        result['UrlDetailData'] = []
        if self.url_detail_data is not None:
            for k1 in self.url_detail_data:
                result['UrlDetailData'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        self.url_detail_data = []
        if m.get('UrlDetailData') is not None:
            for k1 in m.get('UrlDetailData'):
                temp_model = main_models.DescribeUrlObservationDataResponseBodyUrlDetailData()
                self.url_detail_data.append(temp_model.from_map(k1))

        return self

class DescribeUrlObservationDataResponseBodyUrlDetailData(DaraModel):
    def __init__(
        self,
        cls: float = None,
        client_platform: str = None,
        country: str = None,
        fcp: float = None,
        fid: float = None,
        inp: float = None,
        lcp: float = None,
        ttfb: float = None,
        url: str = None,
    ):
        # Measures the maximum layout mutation score for every unexpected layout change that occurs throughout the life of the page.
        self.cls = cls
        # The platform of the device.
        self.client_platform = client_platform
        # The country or region to which the IP address belongs.
        self.country = country
        # Measures the time between when the page is loaded and when any part of the page\\"s content is rendered on the screen. Unit: ms.
        self.fcp = fcp
        # Measures the time between when the user first interacts with the page and when the browser is actually able to start processing an event handler in response to that interaction. Unit: ms.
        self.fid = fid
        # Measures the responsiveness of the page, or how long it takes for the page to respond to user input visibly. Unit: ms.
        self.inp = inp
        # Reports the rendering time of the largest image or text block visible in the viewport. Unit: ms.
        self.lcp = lcp
        # This metric measures the time between when a resource initiates a request and when the first byte of the response starts to arrive. Unit: ms.
        self.ttfb = ttfb
        # The URL of the web page to monitor.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cls is not None:
            result['CLS'] = self.cls

        if self.client_platform is not None:
            result['ClientPlatform'] = self.client_platform

        if self.country is not None:
            result['Country'] = self.country

        if self.fcp is not None:
            result['FCP'] = self.fcp

        if self.fid is not None:
            result['FID'] = self.fid

        if self.inp is not None:
            result['INP'] = self.inp

        if self.lcp is not None:
            result['LCP'] = self.lcp

        if self.ttfb is not None:
            result['TTFB'] = self.ttfb

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CLS') is not None:
            self.cls = m.get('CLS')

        if m.get('ClientPlatform') is not None:
            self.client_platform = m.get('ClientPlatform')

        if m.get('Country') is not None:
            self.country = m.get('Country')

        if m.get('FCP') is not None:
            self.fcp = m.get('FCP')

        if m.get('FID') is not None:
            self.fid = m.get('FID')

        if m.get('INP') is not None:
            self.inp = m.get('INP')

        if m.get('LCP') is not None:
            self.lcp = m.get('LCP')

        if m.get('TTFB') is not None:
            self.ttfb = m.get('TTFB')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

