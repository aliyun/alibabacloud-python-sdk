# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AppInstanceProfile(DaraModel):
    def __init__(
        self,
        application_type: str = None,
        application_type_text: str = None,
        biz_id: str = None,
        commodity_code: str = None,
        customer_service: str = None,
        deploy_area: str = None,
        instance_id: str = None,
        ord_time: str = None,
        order_id: str = None,
        pay_time: str = None,
        seo_site: str = None,
        site_version: str = None,
        site_version_text: str = None,
        source: str = None,
        template_etag: str = None,
        template_id: str = None,
    ):
        self.application_type = application_type
        self.application_type_text = application_type_text
        self.biz_id = biz_id
        self.commodity_code = commodity_code
        self.customer_service = customer_service
        self.deploy_area = deploy_area
        self.instance_id = instance_id
        self.ord_time = ord_time
        self.order_id = order_id
        self.pay_time = pay_time
        self.seo_site = seo_site
        self.site_version = site_version
        self.site_version_text = site_version_text
        self.source = source
        self.template_etag = template_etag
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_type is not None:
            result['ApplicationType'] = self.application_type

        if self.application_type_text is not None:
            result['ApplicationTypeText'] = self.application_type_text

        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        if self.customer_service is not None:
            result['CustomerService'] = self.customer_service

        if self.deploy_area is not None:
            result['DeployArea'] = self.deploy_area

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.ord_time is not None:
            result['OrdTime'] = self.ord_time

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.pay_time is not None:
            result['PayTime'] = self.pay_time

        if self.seo_site is not None:
            result['SeoSite'] = self.seo_site

        if self.site_version is not None:
            result['SiteVersion'] = self.site_version

        if self.site_version_text is not None:
            result['SiteVersionText'] = self.site_version_text

        if self.source is not None:
            result['Source'] = self.source

        if self.template_etag is not None:
            result['TemplateEtag'] = self.template_etag

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationType') is not None:
            self.application_type = m.get('ApplicationType')

        if m.get('ApplicationTypeText') is not None:
            self.application_type_text = m.get('ApplicationTypeText')

        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        if m.get('CustomerService') is not None:
            self.customer_service = m.get('CustomerService')

        if m.get('DeployArea') is not None:
            self.deploy_area = m.get('DeployArea')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OrdTime') is not None:
            self.ord_time = m.get('OrdTime')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('PayTime') is not None:
            self.pay_time = m.get('PayTime')

        if m.get('SeoSite') is not None:
            self.seo_site = m.get('SeoSite')

        if m.get('SiteVersion') is not None:
            self.site_version = m.get('SiteVersion')

        if m.get('SiteVersionText') is not None:
            self.site_version_text = m.get('SiteVersionText')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('TemplateEtag') is not None:
            self.template_etag = m.get('TemplateEtag')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

