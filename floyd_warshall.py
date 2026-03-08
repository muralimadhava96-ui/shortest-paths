"""Backward-compatible wrapper for Floyd-Warshall implementation."""

from shortest_paths.floyd_warshall import floyd_warshall, reconstruct_fw_path

__all__ = ["floyd_warshall", "reconstruct_fw_path"]
