# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pds20220301 import models as main_models
from darabonba.model import DaraModel

class DomainSeniorConfig(DaraModel):
    def __init__(
        self,
        client_download_enable: bool = None,
        csp_frame_ancestors: str = None,
        custom_login_appid: str = None,
        custom_login_url: str = None,
        custom_logout_url: str = None,
        custom_side_link_list: List[main_models.CustomSideLinkConfig] = None,
        home_page_bg_image_url: str = None,
        home_page_footer: str = None,
        home_page_footer_2: str = None,
        home_page_slogan: str = None,
        referer_enable: bool = None,
        wx_txt_list: main_models.WxTrustedDomainConfig = None,
    ):
        self.client_download_enable = client_download_enable
        self.csp_frame_ancestors = csp_frame_ancestors
        self.custom_login_appid = custom_login_appid
        self.custom_login_url = custom_login_url
        self.custom_logout_url = custom_logout_url
        self.custom_side_link_list = custom_side_link_list
        self.home_page_bg_image_url = home_page_bg_image_url
        self.home_page_footer = home_page_footer
        self.home_page_footer_2 = home_page_footer_2
        self.home_page_slogan = home_page_slogan
        self.referer_enable = referer_enable
        self.wx_txt_list = wx_txt_list

    def validate(self):
        if self.custom_side_link_list:
            for v1 in self.custom_side_link_list:
                 if v1:
                    v1.validate()
        if self.wx_txt_list:
            self.wx_txt_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_download_enable is not None:
            result['client_download_enable'] = self.client_download_enable

        if self.csp_frame_ancestors is not None:
            result['csp_frame_ancestors'] = self.csp_frame_ancestors

        if self.custom_login_appid is not None:
            result['custom_login_appid'] = self.custom_login_appid

        if self.custom_login_url is not None:
            result['custom_login_url'] = self.custom_login_url

        if self.custom_logout_url is not None:
            result['custom_logout_url'] = self.custom_logout_url

        result['custom_side_link_list'] = []
        if self.custom_side_link_list is not None:
            for k1 in self.custom_side_link_list:
                result['custom_side_link_list'].append(k1.to_map() if k1 else None)

        if self.home_page_bg_image_url is not None:
            result['home_page_bg_image_url'] = self.home_page_bg_image_url

        if self.home_page_footer is not None:
            result['home_page_footer'] = self.home_page_footer

        if self.home_page_footer_2 is not None:
            result['home_page_footer2'] = self.home_page_footer_2

        if self.home_page_slogan is not None:
            result['home_page_slogan'] = self.home_page_slogan

        if self.referer_enable is not None:
            result['referer_enable'] = self.referer_enable

        if self.wx_txt_list is not None:
            result['wx_txt_list'] = self.wx_txt_list.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('client_download_enable') is not None:
            self.client_download_enable = m.get('client_download_enable')

        if m.get('csp_frame_ancestors') is not None:
            self.csp_frame_ancestors = m.get('csp_frame_ancestors')

        if m.get('custom_login_appid') is not None:
            self.custom_login_appid = m.get('custom_login_appid')

        if m.get('custom_login_url') is not None:
            self.custom_login_url = m.get('custom_login_url')

        if m.get('custom_logout_url') is not None:
            self.custom_logout_url = m.get('custom_logout_url')

        self.custom_side_link_list = []
        if m.get('custom_side_link_list') is not None:
            for k1 in m.get('custom_side_link_list'):
                temp_model = main_models.CustomSideLinkConfig()
                self.custom_side_link_list.append(temp_model.from_map(k1))

        if m.get('home_page_bg_image_url') is not None:
            self.home_page_bg_image_url = m.get('home_page_bg_image_url')

        if m.get('home_page_footer') is not None:
            self.home_page_footer = m.get('home_page_footer')

        if m.get('home_page_footer2') is not None:
            self.home_page_footer_2 = m.get('home_page_footer2')

        if m.get('home_page_slogan') is not None:
            self.home_page_slogan = m.get('home_page_slogan')

        if m.get('referer_enable') is not None:
            self.referer_enable = m.get('referer_enable')

        if m.get('wx_txt_list') is not None:
            temp_model = main_models.WxTrustedDomainConfig()
            self.wx_txt_list = temp_model.from_map(m.get('wx_txt_list'))

        return self

