# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_websitebuild20250429 import models as main_models
from darabonba.model import DaraModel

class AppInstance(DaraModel):
    def __init__(
        self,
        app_sub_type: str = None,
        app_type: str = None,
        biz_id: str = None,
        build_type: str = None,
        deleted: int = None,
        description: str = None,
        design_spec_biz_id: str = None,
        design_spec_id: str = None,
        domain: str = None,
        end_time: str = None,
        esp_biz_id: str = None,
        gmt_create: str = None,
        gmt_delete: str = None,
        gmt_modified: str = None,
        gmt_publish: str = None,
        icon_url: str = None,
        name: str = None,
        profile: main_models.AppInstanceProfile = None,
        site_host: str = None,
        slug: str = None,
        source_type: str = None,
        start_time: str = None,
        status: str = None,
        status_text: str = None,
        thumbnail_url: str = None,
        user_id: str = None,
    ):
        self.app_sub_type = app_sub_type
        self.app_type = app_type
        self.biz_id = biz_id
        self.build_type = build_type
        self.deleted = deleted
        self.description = description
        self.design_spec_biz_id = design_spec_biz_id
        self.design_spec_id = design_spec_id
        self.domain = domain
        self.end_time = end_time
        self.esp_biz_id = esp_biz_id
        self.gmt_create = gmt_create
        self.gmt_delete = gmt_delete
        self.gmt_modified = gmt_modified
        self.gmt_publish = gmt_publish
        self.icon_url = icon_url
        self.name = name
        self.profile = profile
        self.site_host = site_host
        self.slug = slug
        self.source_type = source_type
        self.start_time = start_time
        # trial,draft,live,refunded,expired,released
        self.status = status
        self.status_text = status_text
        self.thumbnail_url = thumbnail_url
        self.user_id = user_id

    def validate(self):
        if self.profile:
            self.profile.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_sub_type is not None:
            result['AppSubType'] = self.app_sub_type

        if self.app_type is not None:
            result['AppType'] = self.app_type

        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.build_type is not None:
            result['BuildType'] = self.build_type

        if self.deleted is not None:
            result['Deleted'] = self.deleted

        if self.description is not None:
            result['Description'] = self.description

        if self.design_spec_biz_id is not None:
            result['DesignSpecBizId'] = self.design_spec_biz_id

        if self.design_spec_id is not None:
            result['DesignSpecId'] = self.design_spec_id

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.esp_biz_id is not None:
            result['EspBizId'] = self.esp_biz_id

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_delete is not None:
            result['GmtDelete'] = self.gmt_delete

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

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

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.status_text is not None:
            result['StatusText'] = self.status_text

        if self.thumbnail_url is not None:
            result['ThumbnailUrl'] = self.thumbnail_url

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppSubType') is not None:
            self.app_sub_type = m.get('AppSubType')

        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')

        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('BuildType') is not None:
            self.build_type = m.get('BuildType')

        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DesignSpecBizId') is not None:
            self.design_spec_biz_id = m.get('DesignSpecBizId')

        if m.get('DesignSpecId') is not None:
            self.design_spec_id = m.get('DesignSpecId')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EspBizId') is not None:
            self.esp_biz_id = m.get('EspBizId')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtDelete') is not None:
            self.gmt_delete = m.get('GmtDelete')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('GmtPublish') is not None:
            self.gmt_publish = m.get('GmtPublish')

        if m.get('IconUrl') is not None:
            self.icon_url = m.get('IconUrl')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Profile') is not None:
            temp_model = main_models.AppInstanceProfile()
            self.profile = temp_model.from_map(m.get('Profile'))

        if m.get('SiteHost') is not None:
            self.site_host = m.get('SiteHost')

        if m.get('Slug') is not None:
            self.slug = m.get('Slug')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StatusText') is not None:
            self.status_text = m.get('StatusText')

        if m.get('ThumbnailUrl') is not None:
            self.thumbnail_url = m.get('ThumbnailUrl')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

