# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_websitebuild20250429 import models as main_models
from darabonba.model import DaraModel

class SyncAppInstanceForPartnerRequest(DaraModel):
    def __init__(
        self,
        app_instance: main_models.SyncAppInstanceForPartnerRequestAppInstance = None,
        event_type: str = None,
        operator: str = None,
        source_biz_id: str = None,
        source_type: str = None,
    ):
        self.app_instance = app_instance
        self.event_type = event_type
        self.operator = operator
        self.source_biz_id = source_biz_id
        self.source_type = source_type

    def validate(self):
        if self.app_instance:
            self.app_instance.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_instance is not None:
            result['AppInstance'] = self.app_instance.to_map()

        if self.event_type is not None:
            result['EventType'] = self.event_type

        if self.operator is not None:
            result['Operator'] = self.operator

        if self.source_biz_id is not None:
            result['SourceBizId'] = self.source_biz_id

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstance') is not None:
            temp_model = main_models.SyncAppInstanceForPartnerRequestAppInstance()
            self.app_instance = temp_model.from_map(m.get('AppInstance'))

        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        if m.get('SourceBizId') is not None:
            self.source_biz_id = m.get('SourceBizId')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        return self

class SyncAppInstanceForPartnerRequestAppInstance(DaraModel):
    def __init__(
        self,
        app_type: str = None,
        biz_id: str = None,
        deleted: str = None,
        domain: str = None,
        end_time: str = None,
        gmt_delete: str = None,
        gmt_publish: str = None,
        icon_url: str = None,
        name: str = None,
        profile: main_models.SyncAppInstanceForPartnerRequestAppInstanceProfile = None,
        site_host: str = None,
        slug: str = None,
        start_time: str = None,
        status: str = None,
        thumbnail_url: str = None,
        user_id: str = None,
    ):
        self.app_type = app_type
        self.biz_id = biz_id
        self.deleted = deleted
        self.domain = domain
        self.end_time = end_time
        self.gmt_delete = gmt_delete
        self.gmt_publish = gmt_publish
        self.icon_url = icon_url
        self.name = name
        self.profile = profile
        # siteId
        self.site_host = site_host
        self.slug = slug
        self.start_time = start_time
        self.status = status
        self.thumbnail_url = thumbnail_url
        # 123123123131232
        self.user_id = user_id

    def validate(self):
        if self.profile:
            self.profile.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_type is not None:
            result['AppType'] = self.app_type

        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.deleted is not None:
            result['Deleted'] = self.deleted

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.gmt_delete is not None:
            result['GmtDelete'] = self.gmt_delete

        if self.gmt_publish is not None:
            result['GmtPublish'] = self.gmt_publish

        if self.icon_url is not None:
            result['IconUrl'] = self.icon_url

        if self.name is not None:
            result['Name'] = self.name

        if self.profile is not None:
            result['Profile'] = self.profile.to_map()

        if self.site_host is not None:
            result['SiteHost'] = self.site_host

        if self.slug is not None:
            result['Slug'] = self.slug

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.thumbnail_url is not None:
            result['ThumbnailUrl'] = self.thumbnail_url

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')

        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('GmtDelete') is not None:
            self.gmt_delete = m.get('GmtDelete')

        if m.get('GmtPublish') is not None:
            self.gmt_publish = m.get('GmtPublish')

        if m.get('IconUrl') is not None:
            self.icon_url = m.get('IconUrl')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Profile') is not None:
            temp_model = main_models.SyncAppInstanceForPartnerRequestAppInstanceProfile()
            self.profile = temp_model.from_map(m.get('Profile'))

        if m.get('SiteHost') is not None:
            self.site_host = m.get('SiteHost')

        if m.get('Slug') is not None:
            self.slug = m.get('Slug')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('ThumbnailUrl') is not None:
            self.thumbnail_url = m.get('ThumbnailUrl')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class SyncAppInstanceForPartnerRequestAppInstanceProfile(DaraModel):
    def __init__(
        self,
        deploy_area: str = None,
        lx_instance_id: str = None,
        order_id: str = None,
        site_version: str = None,
        template_etag: str = None,
        template_id: str = None,
    ):
        self.deploy_area = deploy_area
        self.lx_instance_id = lx_instance_id
        self.order_id = order_id
        self.site_version = site_version
        self.template_etag = template_etag
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.deploy_area is not None:
            result['DeployArea'] = self.deploy_area

        if self.lx_instance_id is not None:
            result['LxInstanceId'] = self.lx_instance_id

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.site_version is not None:
            result['SiteVersion'] = self.site_version

        if self.template_etag is not None:
            result['TemplateEtag'] = self.template_etag

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeployArea') is not None:
            self.deploy_area = m.get('DeployArea')

        if m.get('LxInstanceId') is not None:
            self.lx_instance_id = m.get('LxInstanceId')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('SiteVersion') is not None:
            self.site_version = m.get('SiteVersion')

        if m.get('TemplateEtag') is not None:
            self.template_etag = m.get('TemplateEtag')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

