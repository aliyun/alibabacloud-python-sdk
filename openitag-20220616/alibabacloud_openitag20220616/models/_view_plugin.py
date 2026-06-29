# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from alibabacloud_openitag20220616 import models as main_models
from darabonba.model import DaraModel

class ViewPlugin(DaraModel):
    def __init__(
        self,
        bind_field: str = None,
        convertor: str = None,
        cors_proxy: bool = None,
        display_ori_img: bool = None,
        exif: Dict[str, Any] = None,
        hide: bool = None,
        plugins: Dict[str, Any] = None,
        relation_question_ids: List[str] = None,
        type: str = None,
        visit_info: main_models.ViewPluginVisitInfo = None,
    ):
        # Field mapping to a field in the dataset.
        # 
        # This parameter is required.
        self.bind_field = bind_field
        # Array transformation UDF.
        self.convertor = convertor
        # Whether to handle cross-domain requests.
        # 
        # This parameter is required.
        self.cors_proxy = cors_proxy
        # Whether to display the original image.
        # 
        # This parameter is required.
        self.display_ori_img = display_ori_img
        # Extra information.
        self.exif = exif
        # Whether to hide.
        self.hide = hide
        # Nested widgets.
        self.plugins = plugins
        # List of associated questions.
        self.relation_question_ids = relation_question_ids
        # Widget type. Valid values:
        # - Image: Image.
        # - Text: Text.
        # - Video: Video.
        # - Audio: Audio.
        # 
        # This parameter is required.
        self.type = type
        # Access information.
        self.visit_info = visit_info

    def validate(self):
        if self.visit_info:
            self.visit_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bind_field is not None:
            result['BindField'] = self.bind_field

        if self.convertor is not None:
            result['Convertor'] = self.convertor

        if self.cors_proxy is not None:
            result['CorsProxy'] = self.cors_proxy

        if self.display_ori_img is not None:
            result['DisplayOriImg'] = self.display_ori_img

        if self.exif is not None:
            result['Exif'] = self.exif

        if self.hide is not None:
            result['Hide'] = self.hide

        if self.plugins is not None:
            result['Plugins'] = self.plugins

        if self.relation_question_ids is not None:
            result['RelationQuestionIds'] = self.relation_question_ids

        if self.type is not None:
            result['Type'] = self.type

        if self.visit_info is not None:
            result['VisitInfo'] = self.visit_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindField') is not None:
            self.bind_field = m.get('BindField')

        if m.get('Convertor') is not None:
            self.convertor = m.get('Convertor')

        if m.get('CorsProxy') is not None:
            self.cors_proxy = m.get('CorsProxy')

        if m.get('DisplayOriImg') is not None:
            self.display_ori_img = m.get('DisplayOriImg')

        if m.get('Exif') is not None:
            self.exif = m.get('Exif')

        if m.get('Hide') is not None:
            self.hide = m.get('Hide')

        if m.get('Plugins') is not None:
            self.plugins = m.get('Plugins')

        if m.get('RelationQuestionIds') is not None:
            self.relation_question_ids = m.get('RelationQuestionIds')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('VisitInfo') is not None:
            temp_model = main_models.ViewPluginVisitInfo()
            self.visit_info = temp_model.from_map(m.get('VisitInfo'))

        return self

class ViewPluginVisitInfo(DaraModel):
    def __init__(
        self,
        afts_conf: Dict[str, Any] = None,
        oss_conf: Dict[str, Any] = None,
    ):
        # AFTS configuration.
        self.afts_conf = afts_conf
        # OSS configuration.
        self.oss_conf = oss_conf

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.afts_conf is not None:
            result['aftsConf'] = self.afts_conf

        if self.oss_conf is not None:
            result['ossConf'] = self.oss_conf

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aftsConf') is not None:
            self.afts_conf = m.get('aftsConf')

        if m.get('ossConf') is not None:
            self.oss_conf = m.get('ossConf')

        return self

