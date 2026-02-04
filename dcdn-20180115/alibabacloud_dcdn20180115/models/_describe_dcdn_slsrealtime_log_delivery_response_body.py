# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dcdn20180115 import models as main_models
from darabonba.model import DaraModel

class DescribeDcdnSLSRealtimeLogDeliveryResponseBody(DaraModel):
    def __init__(
        self,
        content: main_models.DescribeDcdnSLSRealtimeLogDeliveryResponseBodyContent = None,
        request_id: str = None,
    ):
        # The configuration results of the domain name.
        self.content = content
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            temp_model = main_models.DescribeDcdnSLSRealtimeLogDeliveryResponseBodyContent()
            self.content = temp_model.from_map(m.get('Content'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDcdnSLSRealtimeLogDeliveryResponseBodyContent(DaraModel):
    def __init__(
        self,
        business_type: str = None,
        data_center: str = None,
        domain_name: str = None,
        field_name: str = None,
        project_name: str = None,
        slslog_store: str = None,
        slsproject: str = None,
        slsregion: str = None,
        sampling_rate: str = None,
        status: str = None,
        type: str = None,
    ):
        # The type of the collected logs. Default value: cdn_log_access_l1. Valid values:
        # 
        # *   **cdn_log_access_l1**: access logs of Dynamic Content Delivery Network (DCDN) points of presence (POPs)
        # *   **cdn_log_origin**: back-to-origin logs
        # *   **cdn_log_er**: EdgeRoutine logs
        self.business_type = business_type
        # The region from which logs were collected.
        self.data_center = data_center
        # The domain names from which logs were collected. You can specify one or more domain names. Separate multiple domain names with commas (,).
        self.domain_name = domain_name
        # The name of the field. For more information about fields in real-time log entries, see [Fields in a real-time log](https://help.aliyun.com/document_detail/324199.html).
        self.field_name = field_name
        # The name of the project.
        self.project_name = project_name
        # The name of the Logstore.
        self.slslog_store = slslog_store
        # The name of the log file.
        self.slsproject = slsproject
        # The region to which logs were delivered.
        self.slsregion = slsregion
        # The sampling rate.
        self.sampling_rate = sampling_rate
        # The status of real-time logs.
        # 
        # *   **success**
        # *   **fail**
        self.status = status
        # The type of log delivery. Only **SLS_POST** is supported.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_type is not None:
            result['BusinessType'] = self.business_type

        if self.data_center is not None:
            result['DataCenter'] = self.data_center

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.field_name is not None:
            result['FieldName'] = self.field_name

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.slslog_store is not None:
            result['SLSLogStore'] = self.slslog_store

        if self.slsproject is not None:
            result['SLSProject'] = self.slsproject

        if self.slsregion is not None:
            result['SLSRegion'] = self.slsregion

        if self.sampling_rate is not None:
            result['SamplingRate'] = self.sampling_rate

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')

        if m.get('DataCenter') is not None:
            self.data_center = m.get('DataCenter')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('FieldName') is not None:
            self.field_name = m.get('FieldName')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('SLSLogStore') is not None:
            self.slslog_store = m.get('SLSLogStore')

        if m.get('SLSProject') is not None:
            self.slsproject = m.get('SLSProject')

        if m.get('SLSRegion') is not None:
            self.slsregion = m.get('SLSRegion')

        if m.get('SamplingRate') is not None:
            self.sampling_rate = m.get('SamplingRate')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

