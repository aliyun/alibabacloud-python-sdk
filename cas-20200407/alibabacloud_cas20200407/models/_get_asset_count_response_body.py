# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAssetCountResponseBody(DaraModel):
    def __init__(
        self,
        aliyun_asset_count: int = None,
        aws_asset_count: int = None,
        buy_certificate_count: int = None,
        domain_asset_count: int = None,
        free_certificate_count: int = None,
        huawei_asset_count: int = None,
        last_point: int = None,
        point: int = None,
        point_ratio: int = None,
        point_time: int = None,
        request_id: str = None,
        tencent_asset_count: int = None,
        upload_certificate_count: int = None,
    ):
        self.aliyun_asset_count = aliyun_asset_count
        self.aws_asset_count = aws_asset_count
        self.buy_certificate_count = buy_certificate_count
        self.domain_asset_count = domain_asset_count
        self.free_certificate_count = free_certificate_count
        self.huawei_asset_count = huawei_asset_count
        self.last_point = last_point
        self.point = point
        self.point_ratio = point_ratio
        self.point_time = point_time
        self.request_id = request_id
        self.tencent_asset_count = tencent_asset_count
        self.upload_certificate_count = upload_certificate_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliyun_asset_count is not None:
            result['AliyunAssetCount'] = self.aliyun_asset_count

        if self.aws_asset_count is not None:
            result['AwsAssetCount'] = self.aws_asset_count

        if self.buy_certificate_count is not None:
            result['BuyCertificateCount'] = self.buy_certificate_count

        if self.domain_asset_count is not None:
            result['DomainAssetCount'] = self.domain_asset_count

        if self.free_certificate_count is not None:
            result['FreeCertificateCount'] = self.free_certificate_count

        if self.huawei_asset_count is not None:
            result['HuaweiAssetCount'] = self.huawei_asset_count

        if self.last_point is not None:
            result['LastPoint'] = self.last_point

        if self.point is not None:
            result['Point'] = self.point

        if self.point_ratio is not None:
            result['PointRatio'] = self.point_ratio

        if self.point_time is not None:
            result['PointTime'] = self.point_time

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.tencent_asset_count is not None:
            result['TencentAssetCount'] = self.tencent_asset_count

        if self.upload_certificate_count is not None:
            result['UploadCertificateCount'] = self.upload_certificate_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunAssetCount') is not None:
            self.aliyun_asset_count = m.get('AliyunAssetCount')

        if m.get('AwsAssetCount') is not None:
            self.aws_asset_count = m.get('AwsAssetCount')

        if m.get('BuyCertificateCount') is not None:
            self.buy_certificate_count = m.get('BuyCertificateCount')

        if m.get('DomainAssetCount') is not None:
            self.domain_asset_count = m.get('DomainAssetCount')

        if m.get('FreeCertificateCount') is not None:
            self.free_certificate_count = m.get('FreeCertificateCount')

        if m.get('HuaweiAssetCount') is not None:
            self.huawei_asset_count = m.get('HuaweiAssetCount')

        if m.get('LastPoint') is not None:
            self.last_point = m.get('LastPoint')

        if m.get('Point') is not None:
            self.point = m.get('Point')

        if m.get('PointRatio') is not None:
            self.point_ratio = m.get('PointRatio')

        if m.get('PointTime') is not None:
            self.point_time = m.get('PointTime')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TencentAssetCount') is not None:
            self.tencent_asset_count = m.get('TencentAssetCount')

        if m.get('UploadCertificateCount') is not None:
            self.upload_certificate_count = m.get('UploadCertificateCount')

        return self

