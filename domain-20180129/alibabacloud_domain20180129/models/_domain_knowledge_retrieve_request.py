# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DomainKnowledgeRetrieveRequest(DaraModel):
    def __init__(
        self,
        global_top_n: int = None,
        keyword: str = None,
        site: str = None,
    ):
        # Le nombre de résultats à renvoyer.
        self.global_top_n = global_top_n
        # Les mots-clés à récupérer.
        # 
        # This parameter is required.
        self.keyword = keyword
        # Les sites de la base de connaissances à interroger, y compris cn pour le national, intl pour l\\"international et all pour tous.
        self.site = site

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.global_top_n is not None:
            result['GlobalTopN'] = self.global_top_n

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.site is not None:
            result['Site'] = self.site

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GlobalTopN') is not None:
            self.global_top_n = m.get('GlobalTopN')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('Site') is not None:
            self.site = m.get('Site')

        return self

