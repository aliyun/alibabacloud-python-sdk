# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cas20200407 import models as main_models
from darabonba.model import DaraModel

class ListCertWarehouseResponseBody(DaraModel):
    def __init__(
        self,
        cert_warehouse_list: List[main_models.ListCertWarehouseResponseBodyCertWarehouseList] = None,
        current_page: int = None,
        request_id: str = None,
        show_size: int = None,
        total_count: int = None,
    ):
        # The certificate application repositories.
        self.cert_warehouse_list = cert_warehouse_list
        # The page number of the returned page. Default value: 1.
        self.current_page = current_page
        # The ID of the request.
        self.request_id = request_id
        # The number of entries returned per page. Default value: 50.
        self.show_size = show_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.cert_warehouse_list:
            for v1 in self.cert_warehouse_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CertWarehouseList'] = []
        if self.cert_warehouse_list is not None:
            for k1 in self.cert_warehouse_list:
                result['CertWarehouseList'].append(k1.to_map() if k1 else None)

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.show_size is not None:
            result['ShowSize'] = self.show_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cert_warehouse_list = []
        if m.get('CertWarehouseList') is not None:
            for k1 in m.get('CertWarehouseList'):
                temp_model = main_models.ListCertWarehouseResponseBodyCertWarehouseList()
                self.cert_warehouse_list.append(temp_model.from_map(k1))

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ShowSize') is not None:
            self.show_size = m.get('ShowSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListCertWarehouseResponseBodyCertWarehouseList(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        instance_id: str = None,
        is_expired: bool = None,
        name: str = None,
        pca_instance_id: str = None,
        qps: int = None,
        type: str = None,
        wh_id: int = None,
    ):
        # The timestamp when the certificate application repository expires. Unit: milliseconds.
        self.end_time = end_time
        # The instance ID of the certificate application repository.
        self.instance_id = instance_id
        # Indicates whether the certificate application repository has expired. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.is_expired = is_expired
        # The name of the certificate application repository.
        self.name = name
        # The instance ID of the private CA.
        self.pca_instance_id = pca_instance_id
        # The queries per second (QPS).
        self.qps = qps
        # The type of the certificate application repository. Valid values:
        # 
        # *   **ssl**: certificate application repository of SSL certificates
        # *   **uploadPCA**: certificate application repository of uploaded private certificates
        # *   **free**: certificate application repository of free certificates, available only on the China site (aliyun.com)
        # *   **aliyunPCA**: certificate application repository of private certificates purchased from Alibaba Cloud Private Certificate Authority (PCA), available only on the China site (aliyun.com)
        # *   **disable**: disabled certificate application repository
        self.type = type
        # The ID of the certificate application repository.
        self.wh_id = wh_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.is_expired is not None:
            result['IsExpired'] = self.is_expired

        if self.name is not None:
            result['Name'] = self.name

        if self.pca_instance_id is not None:
            result['PcaInstanceId'] = self.pca_instance_id

        if self.qps is not None:
            result['Qps'] = self.qps

        if self.type is not None:
            result['Type'] = self.type

        if self.wh_id is not None:
            result['WhId'] = self.wh_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('IsExpired') is not None:
            self.is_expired = m.get('IsExpired')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PcaInstanceId') is not None:
            self.pca_instance_id = m.get('PcaInstanceId')

        if m.get('Qps') is not None:
            self.qps = m.get('Qps')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('WhId') is not None:
            self.wh_id = m.get('WhId')

        return self

