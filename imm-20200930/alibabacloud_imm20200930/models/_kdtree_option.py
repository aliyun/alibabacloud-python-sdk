# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class KdtreeOption(DaraModel):
    def __init__(
        self,
        compression_level: int = None,
        library_name: str = None,
        quantization_bits: int = None,
    ):
        # The compression level. Valid values: 0 to 10. A greater value specifies a higher compression ratio and ensures better detail effects.
        self.compression_level = compression_level
        # The name of the library supported by a k-d tree. Set the value to draco. Default value: draco.
        self.library_name = library_name
        # The number of bits for quantization. Valid values: 0 to 31. A greater value ensures that more details are retained. A value of 0 specifies that vertex compression is not performed.
        self.quantization_bits = quantization_bits

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.compression_level is not None:
            result['CompressionLevel'] = self.compression_level

        if self.library_name is not None:
            result['LibraryName'] = self.library_name

        if self.quantization_bits is not None:
            result['QuantizationBits'] = self.quantization_bits

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompressionLevel') is not None:
            self.compression_level = m.get('CompressionLevel')

        if m.get('LibraryName') is not None:
            self.library_name = m.get('LibraryName')

        if m.get('QuantizationBits') is not None:
            self.quantization_bits = m.get('QuantizationBits')

        return self

