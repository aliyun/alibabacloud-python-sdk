# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SaveSingleTaskForSaveArtExtensionRequest(DaraModel):
    def __init__(
        self,
        date_or_period: str = None,
        dimensions: str = None,
        domain_name: str = None,
        features: str = None,
        inscriptions_and_markings: str = None,
        lang: str = None,
        maker: str = None,
        materials_and_techniques: str = None,
        object_type: str = None,
        reference: str = None,
        subject: str = None,
        title: str = None,
    ):
        self.date_or_period = date_or_period
        self.dimensions = dimensions
        # This parameter is required.
        self.domain_name = domain_name
        self.features = features
        self.inscriptions_and_markings = inscriptions_and_markings
        self.lang = lang
        self.maker = maker
        self.materials_and_techniques = materials_and_techniques
        self.object_type = object_type
        self.reference = reference
        self.subject = subject
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.date_or_period is not None:
            result['DateOrPeriod'] = self.date_or_period

        if self.dimensions is not None:
            result['Dimensions'] = self.dimensions

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.features is not None:
            result['Features'] = self.features

        if self.inscriptions_and_markings is not None:
            result['InscriptionsAndMarkings'] = self.inscriptions_and_markings

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.maker is not None:
            result['Maker'] = self.maker

        if self.materials_and_techniques is not None:
            result['MaterialsAndTechniques'] = self.materials_and_techniques

        if self.object_type is not None:
            result['ObjectType'] = self.object_type

        if self.reference is not None:
            result['Reference'] = self.reference

        if self.subject is not None:
            result['Subject'] = self.subject

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DateOrPeriod') is not None:
            self.date_or_period = m.get('DateOrPeriod')

        if m.get('Dimensions') is not None:
            self.dimensions = m.get('Dimensions')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('Features') is not None:
            self.features = m.get('Features')

        if m.get('InscriptionsAndMarkings') is not None:
            self.inscriptions_and_markings = m.get('InscriptionsAndMarkings')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Maker') is not None:
            self.maker = m.get('Maker')

        if m.get('MaterialsAndTechniques') is not None:
            self.materials_and_techniques = m.get('MaterialsAndTechniques')

        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')

        if m.get('Reference') is not None:
            self.reference = m.get('Reference')

        if m.get('Subject') is not None:
            self.subject = m.get('Subject')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

