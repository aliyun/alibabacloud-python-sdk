# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_websitebuild20250429 import models as main_models
from darabonba.model import DaraModel

class ListAppTemplatesResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        allow_retry: bool = None,
        app_name: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_args: List[Any] = None,
        max_results: int = None,
        module: main_models.ListAppTemplatesResponseBodyModule = None,
        next_token: str = None,
        request_id: str = None,
        root_error_code: str = None,
        root_error_msg: str = None,
        synchro: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.allow_retry = allow_retry
        self.app_name = app_name
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_args = error_args
        self.max_results = max_results
        self.module = module
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id
        self.root_error_code = root_error_code
        self.root_error_msg = root_error_msg
        self.synchro = synchro

    def validate(self):
        if self.module:
            self.module.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.allow_retry is not None:
            result['AllowRetry'] = self.allow_retry

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code

        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message

        if self.error_args is not None:
            result['ErrorArgs'] = self.error_args

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.module is not None:
            result['Module'] = self.module.to_map()

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.root_error_code is not None:
            result['RootErrorCode'] = self.root_error_code

        if self.root_error_msg is not None:
            result['RootErrorMsg'] = self.root_error_msg

        if self.synchro is not None:
            result['Synchro'] = self.synchro

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('AllowRetry') is not None:
            self.allow_retry = m.get('AllowRetry')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')

        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')

        if m.get('ErrorArgs') is not None:
            self.error_args = m.get('ErrorArgs')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('Module') is not None:
            temp_model = main_models.ListAppTemplatesResponseBodyModule()
            self.module = temp_model.from_map(m.get('Module'))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RootErrorCode') is not None:
            self.root_error_code = m.get('RootErrorCode')

        if m.get('RootErrorMsg') is not None:
            self.root_error_msg = m.get('RootErrorMsg')

        if m.get('Synchro') is not None:
            self.synchro = m.get('Synchro')

        return self

class ListAppTemplatesResponseBodyModule(DaraModel):
    def __init__(
        self,
        current_page_num: int = None,
        data: List[main_models.ListAppTemplatesResponseBodyModuleData] = None,
        next: main_models.ListAppTemplatesResponseBodyModuleNext = None,
        next_page: bool = None,
        page_size: int = None,
        pre_page: bool = None,
        result_limit: bool = None,
        total_item_num: int = None,
        total_page_num: int = None,
    ):
        self.current_page_num = current_page_num
        self.data = data
        self.next = next
        self.next_page = next_page
        self.page_size = page_size
        self.pre_page = pre_page
        self.result_limit = result_limit
        self.total_item_num = total_item_num
        self.total_page_num = total_page_num

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()
        if self.next:
            self.next.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.next is not None:
            result['Next'] = self.next.to_map()

        if self.next_page is not None:
            result['NextPage'] = self.next_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.pre_page is not None:
            result['PrePage'] = self.pre_page

        if self.result_limit is not None:
            result['ResultLimit'] = self.result_limit

        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num

        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListAppTemplatesResponseBodyModuleData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Next') is not None:
            temp_model = main_models.ListAppTemplatesResponseBodyModuleNext()
            self.next = temp_model.from_map(m.get('Next'))

        if m.get('NextPage') is not None:
            self.next_page = m.get('NextPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PrePage') is not None:
            self.pre_page = m.get('PrePage')

        if m.get('ResultLimit') is not None:
            self.result_limit = m.get('ResultLimit')

        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')

        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')

        return self

class ListAppTemplatesResponseBodyModuleNext(DaraModel):
    def __init__(
        self,
        app_type: str = None,
        biz_id: str = None,
        color_scheme: str = None,
        color_scheme_name: str = None,
        copy_count: int = None,
        creator: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        industry: str = None,
        industry_name: str = None,
        last_modifier: str = None,
        like_count: int = None,
        liked: bool = None,
        metadata: str = None,
        preview_url: str = None,
        product_version: str = None,
        product_version_name: str = None,
        share_count: int = None,
        status: str = None,
        template_id: str = None,
        template_name: str = None,
        thumbnail_url: str = None,
        view_count: int = None,
        weight: int = None,
    ):
        self.app_type = app_type
        self.biz_id = biz_id
        self.color_scheme = color_scheme
        self.color_scheme_name = color_scheme_name
        self.copy_count = copy_count
        self.creator = creator
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.industry = industry
        self.industry_name = industry_name
        self.last_modifier = last_modifier
        self.like_count = like_count
        self.liked = liked
        self.metadata = metadata
        self.preview_url = preview_url
        self.product_version = product_version
        self.product_version_name = product_version_name
        self.share_count = share_count
        self.status = status
        self.template_id = template_id
        self.template_name = template_name
        self.thumbnail_url = thumbnail_url
        self.view_count = view_count
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_type is not None:
            result['AppType'] = self.app_type

        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.color_scheme is not None:
            result['ColorScheme'] = self.color_scheme

        if self.color_scheme_name is not None:
            result['ColorSchemeName'] = self.color_scheme_name

        if self.copy_count is not None:
            result['CopyCount'] = self.copy_count

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.industry is not None:
            result['Industry'] = self.industry

        if self.industry_name is not None:
            result['IndustryName'] = self.industry_name

        if self.last_modifier is not None:
            result['LastModifier'] = self.last_modifier

        if self.like_count is not None:
            result['LikeCount'] = self.like_count

        if self.liked is not None:
            result['Liked'] = self.liked

        if self.metadata is not None:
            result['Metadata'] = self.metadata

        if self.preview_url is not None:
            result['PreviewUrl'] = self.preview_url

        if self.product_version is not None:
            result['ProductVersion'] = self.product_version

        if self.product_version_name is not None:
            result['ProductVersionName'] = self.product_version_name

        if self.share_count is not None:
            result['ShareCount'] = self.share_count

        if self.status is not None:
            result['Status'] = self.status

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.thumbnail_url is not None:
            result['ThumbnailUrl'] = self.thumbnail_url

        if self.view_count is not None:
            result['ViewCount'] = self.view_count

        if self.weight is not None:
            result['Weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')

        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('ColorScheme') is not None:
            self.color_scheme = m.get('ColorScheme')

        if m.get('ColorSchemeName') is not None:
            self.color_scheme_name = m.get('ColorSchemeName')

        if m.get('CopyCount') is not None:
            self.copy_count = m.get('CopyCount')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Industry') is not None:
            self.industry = m.get('Industry')

        if m.get('IndustryName') is not None:
            self.industry_name = m.get('IndustryName')

        if m.get('LastModifier') is not None:
            self.last_modifier = m.get('LastModifier')

        if m.get('LikeCount') is not None:
            self.like_count = m.get('LikeCount')

        if m.get('Liked') is not None:
            self.liked = m.get('Liked')

        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')

        if m.get('PreviewUrl') is not None:
            self.preview_url = m.get('PreviewUrl')

        if m.get('ProductVersion') is not None:
            self.product_version = m.get('ProductVersion')

        if m.get('ProductVersionName') is not None:
            self.product_version_name = m.get('ProductVersionName')

        if m.get('ShareCount') is not None:
            self.share_count = m.get('ShareCount')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('ThumbnailUrl') is not None:
            self.thumbnail_url = m.get('ThumbnailUrl')

        if m.get('ViewCount') is not None:
            self.view_count = m.get('ViewCount')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        return self

class ListAppTemplatesResponseBodyModuleData(DaraModel):
    def __init__(
        self,
        app_type: str = None,
        biz_id: str = None,
        color_scheme: str = None,
        color_scheme_name: str = None,
        copy_count: int = None,
        creator: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        id: int = None,
        industry: str = None,
        industry_name: str = None,
        last_modifier: str = None,
        like_count: int = None,
        liked: bool = None,
        metadata: str = None,
        preview_url: str = None,
        product_version: str = None,
        product_version_name: str = None,
        share_count: int = None,
        status: str = None,
        template_id: str = None,
        template_name: str = None,
        thumbnail_url: str = None,
        view_count: int = None,
        weight: int = None,
    ):
        self.app_type = app_type
        self.biz_id = biz_id
        self.color_scheme = color_scheme
        self.color_scheme_name = color_scheme_name
        self.copy_count = copy_count
        self.creator = creator
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ss.SSSZ
        self.gmt_create_time = gmt_create_time
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ss.SSSZ
        self.gmt_modified_time = gmt_modified_time
        self.id = id
        self.industry = industry
        self.industry_name = industry_name
        self.last_modifier = last_modifier
        self.like_count = like_count
        self.liked = liked
        self.metadata = metadata
        self.preview_url = preview_url
        self.product_version = product_version
        self.product_version_name = product_version_name
        self.share_count = share_count
        self.status = status
        self.template_id = template_id
        self.template_name = template_name
        self.thumbnail_url = thumbnail_url
        self.view_count = view_count
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_type is not None:
            result['AppType'] = self.app_type

        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.color_scheme is not None:
            result['ColorScheme'] = self.color_scheme

        if self.color_scheme_name is not None:
            result['ColorSchemeName'] = self.color_scheme_name

        if self.copy_count is not None:
            result['CopyCount'] = self.copy_count

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time

        if self.id is not None:
            result['Id'] = self.id

        if self.industry is not None:
            result['Industry'] = self.industry

        if self.industry_name is not None:
            result['IndustryName'] = self.industry_name

        if self.last_modifier is not None:
            result['LastModifier'] = self.last_modifier

        if self.like_count is not None:
            result['LikeCount'] = self.like_count

        if self.liked is not None:
            result['Liked'] = self.liked

        if self.metadata is not None:
            result['Metadata'] = self.metadata

        if self.preview_url is not None:
            result['PreviewUrl'] = self.preview_url

        if self.product_version is not None:
            result['ProductVersion'] = self.product_version

        if self.product_version_name is not None:
            result['ProductVersionName'] = self.product_version_name

        if self.share_count is not None:
            result['ShareCount'] = self.share_count

        if self.status is not None:
            result['Status'] = self.status

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.thumbnail_url is not None:
            result['ThumbnailUrl'] = self.thumbnail_url

        if self.view_count is not None:
            result['ViewCount'] = self.view_count

        if self.weight is not None:
            result['Weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')

        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('ColorScheme') is not None:
            self.color_scheme = m.get('ColorScheme')

        if m.get('ColorSchemeName') is not None:
            self.color_scheme_name = m.get('ColorSchemeName')

        if m.get('CopyCount') is not None:
            self.copy_count = m.get('CopyCount')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Industry') is not None:
            self.industry = m.get('Industry')

        if m.get('IndustryName') is not None:
            self.industry_name = m.get('IndustryName')

        if m.get('LastModifier') is not None:
            self.last_modifier = m.get('LastModifier')

        if m.get('LikeCount') is not None:
            self.like_count = m.get('LikeCount')

        if m.get('Liked') is not None:
            self.liked = m.get('Liked')

        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')

        if m.get('PreviewUrl') is not None:
            self.preview_url = m.get('PreviewUrl')

        if m.get('ProductVersion') is not None:
            self.product_version = m.get('ProductVersion')

        if m.get('ProductVersionName') is not None:
            self.product_version_name = m.get('ProductVersionName')

        if m.get('ShareCount') is not None:
            self.share_count = m.get('ShareCount')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('ThumbnailUrl') is not None:
            self.thumbnail_url = m.get('ThumbnailUrl')

        if m.get('ViewCount') is not None:
            self.view_count = m.get('ViewCount')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        return self

