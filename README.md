# oprune

## Overview

oprune is a simple utility to clean up unused attachments from an Obsidian vault.

It is intended to be installed via pipx and run as a cli utility.

To detect unused attachments oprune will scan every file in the path provided as an argument for references to attachments. Any attachments found in the vault that are not referenced will be marked for deletion.

Each file must be confirmed for deletion individually to prevent the liklihood something important is deleted.

## Installation

oprune should be installed with [pipx](https://pipx.pypa.io/stable/) with the following command:

`pipx install git+https://github.com/jmarkIT/oprune`

## Usage

oprune accepts a single argument, the path to your Obsidian vault

`oprune {path_to_obsidian_vault}`

Any unused attachments will have their full path printed to the terminal to confirm deletion.
