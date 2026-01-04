# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeElasticQpsRecordResponseBody(DaraModel):
    def __init__(
        self,
        elastic_qps_list: List[main_models.DescribeElasticQpsRecordResponseBodyElasticQpsList] = None,
        request_id: str = None,
    ):
        # The QPS information about the instance.
        self.elastic_qps_list = elastic_qps_list
        # The request ID, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.elastic_qps_list:
            for v1 in self.elastic_qps_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ElasticQpsList'] = []
        if self.elastic_qps_list is not None:
            for k1 in self.elastic_qps_list:
                result['ElasticQpsList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.elastic_qps_list = []
        if m.get('ElasticQpsList') is not None:
            for k1 in m.get('ElasticQpsList'):
                temp_model = main_models.DescribeElasticQpsRecordResponseBodyElasticQpsList()
                self.elastic_qps_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeElasticQpsRecordResponseBodyElasticQpsList(DaraModel):
    def __init__(
        self,
        date: int = None,
        instance_id: str = None,
        ip: str = None,
        ops_elastic_qps: int = None,
        ops_qps: int = None,
        origin_qps: int = None,
        qps: int = None,
        qps_peak: int = None,
        status: int = None,
    ):
        # The timestamp. Unit: milliseconds.
        self.date = date
        # The ID of the Anti-DDoS Proxy instance.
        self.instance_id = instance_id
        # The IP address of the Anti-DDoS Proxy instance.
        self.ip = ip
        # The burstable QPS value. A value of 0 indicates that the burstable QPS feature is not enabled.
        self.ops_elastic_qps = ops_elastic_qps
        # The service QPS (active).
        self.ops_qps = ops_qps
        # The service QPS (purchased).
        self.origin_qps = origin_qps
        # The daily peak 95th percentile QPS.
        self.qps = qps
        # The daily peak traffic.
        self.qps_peak = qps_peak
        # Indicates whether the instance has expired or is released. Valid values:
        # 
        # *   **1**: The instance runs as expected.
        # *   **2**: The instance has expired.
        # *   **4**: The instance is released.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.date is not None:
            result['Date'] = self.date

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.ops_elastic_qps is not None:
            result['OpsElasticQps'] = self.ops_elastic_qps

        if self.ops_qps is not None:
            result['OpsQps'] = self.ops_qps

        if self.origin_qps is not None:
            result['OriginQps'] = self.origin_qps

        if self.qps is not None:
            result['Qps'] = self.qps

        if self.qps_peak is not None:
            result['QpsPeak'] = self.qps_peak

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Date') is not None:
            self.date = m.get('Date')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('OpsElasticQps') is not None:
            self.ops_elastic_qps = m.get('OpsElasticQps')

        if m.get('OpsQps') is not None:
            self.ops_qps = m.get('OpsQps')

        if m.get('OriginQps') is not None:
            self.origin_qps = m.get('OriginQps')

        if m.get('Qps') is not None:
            self.qps = m.get('Qps')

        if m.get('QpsPeak') is not None:
            self.qps_peak = m.get('QpsPeak')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

