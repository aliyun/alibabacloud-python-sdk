# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ModuleFlightItemListBestPriceItemShoppingItemMapValueCabinQuantityValue(DaraModel):
    def __init__(
        self,
        cabin: str = None,
        cabin_class: str = None,
        cabin_class_name: str = None,
        cabin_class_memo: str = None,
        specification: str = None,
        quantity: str = None,
        link_cabins: List[str] = None,
        reshop_change_cabin: bool = None,
        child_cabin_type: int = None,
        infant_basic_cabin: str = None,
        inner_cabin_class: int = None,
    ):
        self.cabin = cabin
        self.cabin_class = cabin_class
        self.cabin_class_name = cabin_class_name
        self.cabin_class_memo = cabin_class_memo
        self.specification = specification
        self.quantity = quantity
        self.link_cabins = link_cabins
        self.reshop_change_cabin = reshop_change_cabin
        self.child_cabin_type = child_cabin_type
        self.infant_basic_cabin = infant_basic_cabin
        self.inner_cabin_class = inner_cabin_class

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cabin is not None:
            result['cabin'] = self.cabin

        if self.cabin_class is not None:
            result['cabin_class'] = self.cabin_class

        if self.cabin_class_name is not None:
            result['cabin_class_name'] = self.cabin_class_name

        if self.cabin_class_memo is not None:
            result['cabin_class_memo'] = self.cabin_class_memo

        if self.specification is not None:
            result['specification'] = self.specification

        if self.quantity is not None:
            result['quantity'] = self.quantity

        if self.link_cabins is not None:
            result['link_cabins'] = self.link_cabins

        if self.reshop_change_cabin is not None:
            result['reshop_change_cabin'] = self.reshop_change_cabin

        if self.child_cabin_type is not None:
            result['child_cabin_type'] = self.child_cabin_type

        if self.infant_basic_cabin is not None:
            result['infant_basic_cabin'] = self.infant_basic_cabin

        if self.inner_cabin_class is not None:
            result['inner_cabin_class'] = self.inner_cabin_class

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cabin') is not None:
            self.cabin = m.get('cabin')

        if m.get('cabin_class') is not None:
            self.cabin_class = m.get('cabin_class')

        if m.get('cabin_class_name') is not None:
            self.cabin_class_name = m.get('cabin_class_name')

        if m.get('cabin_class_memo') is not None:
            self.cabin_class_memo = m.get('cabin_class_memo')

        if m.get('specification') is not None:
            self.specification = m.get('specification')

        if m.get('quantity') is not None:
            self.quantity = m.get('quantity')

        if m.get('link_cabins') is not None:
            self.link_cabins = m.get('link_cabins')

        if m.get('reshop_change_cabin') is not None:
            self.reshop_change_cabin = m.get('reshop_change_cabin')

        if m.get('child_cabin_type') is not None:
            self.child_cabin_type = m.get('child_cabin_type')

        if m.get('infant_basic_cabin') is not None:
            self.infant_basic_cabin = m.get('infant_basic_cabin')

        if m.get('inner_cabin_class') is not None:
            self.inner_cabin_class = m.get('inner_cabin_class')

        return self

