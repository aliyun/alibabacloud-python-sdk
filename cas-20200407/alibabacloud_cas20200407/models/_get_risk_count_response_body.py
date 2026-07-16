# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetRiskCountResponseBody(DaraModel):
    def __init__(
        self,
        aliyun_asset_certificate_expired_count: int = None,
        aliyun_asset_certificate_will_expired_count: int = None,
        buy_certificate_expire_count: int = None,
        buy_certificate_not_deployment_count: int = None,
        buy_certificate_not_trustee_count: int = None,
        buy_certificate_will_expired_count: int = None,
        buy_checked_fail_count: int = None,
        domain_asset_not_monitor_count: int = None,
        free_certificate_expire_count: int = None,
        free_certificate_not_deployment_count: int = None,
        free_certificate_will_expired_count: int = None,
        free_checked_fail_count: int = None,
        multi_cloud_asset_certificate_expired_count: int = None,
        multi_cloud_asset_certificate_will_expired_count: int = None,
        request_id: str = None,
        upload_certificate_expire_count: int = None,
        upload_certificate_not_deployment_count: int = None,
        upload_certificate_not_notice_count: int = None,
        upload_certificate_will_expired_count: int = None,
    ):
        # Number of expired Alibaba Cloud certificates.
        self.aliyun_asset_certificate_expired_count = aliyun_asset_certificate_expired_count
        # Number of Alibaba Cloud certificates that will expire soon.
        self.aliyun_asset_certificate_will_expired_count = aliyun_asset_certificate_will_expired_count
        # Number of expired paid certificates.
        self.buy_certificate_expire_count = buy_certificate_expire_count
        # Number of paid certificates not deployed.
        self.buy_certificate_not_deployment_count = buy_certificate_not_deployment_count
        # Number of paid certificates not managed.
        self.buy_certificate_not_trustee_count = buy_certificate_not_trustee_count
        # Number of paid certificates that will expire soon.
        self.buy_certificate_will_expired_count = buy_certificate_will_expired_count
        # Number of failed paid certificate orders.
        self.buy_checked_fail_count = buy_checked_fail_count
        # Number of domains without monitoring configured.
        self.domain_asset_not_monitor_count = domain_asset_not_monitor_count
        # Number of expired free certificates.
        self.free_certificate_expire_count = free_certificate_expire_count
        # Number of free certificates not deployed.
        self.free_certificate_not_deployment_count = free_certificate_not_deployment_count
        # Number of free certificates that will expire soon.
        self.free_certificate_will_expired_count = free_certificate_will_expired_count
        # Number of failed free certificate orders.
        self.free_checked_fail_count = free_checked_fail_count
        # Number of expired multicloud certificates.
        self.multi_cloud_asset_certificate_expired_count = multi_cloud_asset_certificate_expired_count
        # Number of multicloud certificates that will expire soon.
        self.multi_cloud_asset_certificate_will_expired_count = multi_cloud_asset_certificate_will_expired_count
        # The ID of this API call. Alibaba Cloud generates this unique identifier for each request. Use it to troubleshoot and locate issues.
        self.request_id = request_id
        # Number of expired uploaded certificates.
        self.upload_certificate_expire_count = upload_certificate_expire_count
        # Number of uploaded certificates not deployed.
        self.upload_certificate_not_deployment_count = upload_certificate_not_deployment_count
        # Number of uploaded certificates without alerting configured.
        self.upload_certificate_not_notice_count = upload_certificate_not_notice_count
        # Number of uploaded certificates that will expire soon.
        self.upload_certificate_will_expired_count = upload_certificate_will_expired_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliyun_asset_certificate_expired_count is not None:
            result['AliyunAssetCertificateExpiredCount'] = self.aliyun_asset_certificate_expired_count

        if self.aliyun_asset_certificate_will_expired_count is not None:
            result['AliyunAssetCertificateWillExpiredCount'] = self.aliyun_asset_certificate_will_expired_count

        if self.buy_certificate_expire_count is not None:
            result['BuyCertificateExpireCount'] = self.buy_certificate_expire_count

        if self.buy_certificate_not_deployment_count is not None:
            result['BuyCertificateNotDeploymentCount'] = self.buy_certificate_not_deployment_count

        if self.buy_certificate_not_trustee_count is not None:
            result['BuyCertificateNotTrusteeCount'] = self.buy_certificate_not_trustee_count

        if self.buy_certificate_will_expired_count is not None:
            result['BuyCertificateWillExpiredCount'] = self.buy_certificate_will_expired_count

        if self.buy_checked_fail_count is not None:
            result['BuyCheckedFailCount'] = self.buy_checked_fail_count

        if self.domain_asset_not_monitor_count is not None:
            result['DomainAssetNotMonitorCount'] = self.domain_asset_not_monitor_count

        if self.free_certificate_expire_count is not None:
            result['FreeCertificateExpireCount'] = self.free_certificate_expire_count

        if self.free_certificate_not_deployment_count is not None:
            result['FreeCertificateNotDeploymentCount'] = self.free_certificate_not_deployment_count

        if self.free_certificate_will_expired_count is not None:
            result['FreeCertificateWillExpiredCount'] = self.free_certificate_will_expired_count

        if self.free_checked_fail_count is not None:
            result['FreeCheckedFailCount'] = self.free_checked_fail_count

        if self.multi_cloud_asset_certificate_expired_count is not None:
            result['MultiCloudAssetCertificateExpiredCount'] = self.multi_cloud_asset_certificate_expired_count

        if self.multi_cloud_asset_certificate_will_expired_count is not None:
            result['MultiCloudAssetCertificateWillExpiredCount'] = self.multi_cloud_asset_certificate_will_expired_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.upload_certificate_expire_count is not None:
            result['UploadCertificateExpireCount'] = self.upload_certificate_expire_count

        if self.upload_certificate_not_deployment_count is not None:
            result['UploadCertificateNotDeploymentCount'] = self.upload_certificate_not_deployment_count

        if self.upload_certificate_not_notice_count is not None:
            result['UploadCertificateNotNoticeCount'] = self.upload_certificate_not_notice_count

        if self.upload_certificate_will_expired_count is not None:
            result['UploadCertificateWillExpiredCount'] = self.upload_certificate_will_expired_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunAssetCertificateExpiredCount') is not None:
            self.aliyun_asset_certificate_expired_count = m.get('AliyunAssetCertificateExpiredCount')

        if m.get('AliyunAssetCertificateWillExpiredCount') is not None:
            self.aliyun_asset_certificate_will_expired_count = m.get('AliyunAssetCertificateWillExpiredCount')

        if m.get('BuyCertificateExpireCount') is not None:
            self.buy_certificate_expire_count = m.get('BuyCertificateExpireCount')

        if m.get('BuyCertificateNotDeploymentCount') is not None:
            self.buy_certificate_not_deployment_count = m.get('BuyCertificateNotDeploymentCount')

        if m.get('BuyCertificateNotTrusteeCount') is not None:
            self.buy_certificate_not_trustee_count = m.get('BuyCertificateNotTrusteeCount')

        if m.get('BuyCertificateWillExpiredCount') is not None:
            self.buy_certificate_will_expired_count = m.get('BuyCertificateWillExpiredCount')

        if m.get('BuyCheckedFailCount') is not None:
            self.buy_checked_fail_count = m.get('BuyCheckedFailCount')

        if m.get('DomainAssetNotMonitorCount') is not None:
            self.domain_asset_not_monitor_count = m.get('DomainAssetNotMonitorCount')

        if m.get('FreeCertificateExpireCount') is not None:
            self.free_certificate_expire_count = m.get('FreeCertificateExpireCount')

        if m.get('FreeCertificateNotDeploymentCount') is not None:
            self.free_certificate_not_deployment_count = m.get('FreeCertificateNotDeploymentCount')

        if m.get('FreeCertificateWillExpiredCount') is not None:
            self.free_certificate_will_expired_count = m.get('FreeCertificateWillExpiredCount')

        if m.get('FreeCheckedFailCount') is not None:
            self.free_checked_fail_count = m.get('FreeCheckedFailCount')

        if m.get('MultiCloudAssetCertificateExpiredCount') is not None:
            self.multi_cloud_asset_certificate_expired_count = m.get('MultiCloudAssetCertificateExpiredCount')

        if m.get('MultiCloudAssetCertificateWillExpiredCount') is not None:
            self.multi_cloud_asset_certificate_will_expired_count = m.get('MultiCloudAssetCertificateWillExpiredCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('UploadCertificateExpireCount') is not None:
            self.upload_certificate_expire_count = m.get('UploadCertificateExpireCount')

        if m.get('UploadCertificateNotDeploymentCount') is not None:
            self.upload_certificate_not_deployment_count = m.get('UploadCertificateNotDeploymentCount')

        if m.get('UploadCertificateNotNoticeCount') is not None:
            self.upload_certificate_not_notice_count = m.get('UploadCertificateNotNoticeCount')

        if m.get('UploadCertificateWillExpiredCount') is not None:
            self.upload_certificate_will_expired_count = m.get('UploadCertificateWillExpiredCount')

        return self

