from flask import Flask, jsonify, request, render_template
import sqlite3

app = Flask(__name__)
