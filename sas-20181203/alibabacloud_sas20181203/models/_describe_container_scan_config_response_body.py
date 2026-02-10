# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeContainerScanConfigResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeContainerScanConfigResponseBodyData = None,
        http_status_code: int = None,
        request_id: str = None,
    ):
        # The response parameters.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.DescribeContainerScanConfigResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeContainerScanConfigResponseBodyData(DaraModel):
    def __init__(
        self,
        all_count: int = None,
        app_names: str = None,
        choose_count: int = None,
        cluster_id: str = None,
        cluster_name: str = None,
    ):
        # The total number of container applications in the cluster.
        self.all_count = all_count
        # The names of the container applications.
        self.app_names = app_names
        # The number of selected container applications.
        self.choose_count = choose_count
        # The cluster ID.
        self.cluster_id = cluster_id
        # The name of the cluster.
        self.cluster_name = cluster_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.all_count is not None:
            result['AllCount'] = self.all_count

        if self.app_names is not None:
            result['AppNames'] = self.app_names

        if self.choose_count is not None:
            result['ChooseCount'] = self.choose_count

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllCount') is not None:
            self.all_count = m.get('AllCount')

        if m.get('AppNames') is not None:
            self.app_names = m.get('AppNames')

        if m.get('ChooseCount') is not None:
            self.choose_count = m.get('ChooseCount')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        return self

